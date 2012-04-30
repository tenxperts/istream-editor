/* Anshuman - opencv algorithm for istream - 09 Feb 2012 */

#include <cv.h> /* required to use OpenCV */ 
#include <highgui.h> /* required to use OpenCV's highgui */
#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;
using namespace cv;

/* Determine if pixels differ in two matrices - use a standard threshold */
int pixel_differ(Mat& mat1, Mat& mat2) 
{
	/* Check conditions like rows and cols are not matching */
	if (!((mat1.rows == mat2.rows) && (mat1.cols == mat2.cols)))
		return  -1;
	/* Check if the matrices are not 8 bit 3 channel images */
	if (mat1.type() != CV_8UC3)
		return -1;
	if (mat2.type() != CV_8UC3)
		return -1;
	/*Define pixel threshold values */
	unsigned char red_threshold = 0x0f;
	unsigned char green_threshold = 0x0f;
	unsigned char blue_threshold = 0x0f;

	/* Split the matrices into three channels */
	std::vector<Mat> three_channels_mat1;
	cv::split(mat1, three_channels_mat1);
	std::vector<Mat> three_channels_mat2;
	cv::split(mat2, three_channels_mat2);
	int i, j;
	int retval = 0;
	for(i=0; i<mat1.rows; i++) {
		for(j=0; j<mat1.cols; j++) {
			
			/* Extract the channel values */
			uchar pixel_1_r = three_channels_mat1[2].at<uchar>(i,j);
			uchar pixel_1_g = three_channels_mat1[1].at<uchar>(i,j);
			uchar pixel_1_b = three_channels_mat1[0].at<uchar>(i,j);

			uchar pixel_2_r = three_channels_mat2[2].at<uchar>(i,j);
			uchar pixel_2_g = three_channels_mat2[1].at<uchar>(i,j);
			uchar pixel_2_b = three_channels_mat2[0].at<uchar>(i,j);
			
			/*Only if each of the channel values for the frames differ by 
		 	* their respctive thresholds we call the pixels different  */
			uchar pixel_diff_r;
			if (pixel_2_r >= pixel_1_r)	
				pixel_diff_r = pixel_2_r - pixel_1_r;
			else
				pixel_diff_r = pixel_1_r - pixel_2_r;
			if (pixel_diff_r > red_threshold) 
			{
				unsigned char pixel_diff_g;
				if (pixel_2_g >= pixel_1_g)	
					pixel_diff_g = pixel_2_g - pixel_1_g;
				else
					pixel_diff_g = pixel_1_g - pixel_2_g;
				if (pixel_diff_g > green_threshold)
				{
					unsigned char pixel_diff_b;
					if (pixel_2_b >= pixel_1_b)	
						pixel_diff_b = pixel_2_b - pixel_1_b;
					else
						pixel_diff_b = pixel_1_b - pixel_2_b;
			
					if (pixel_diff_b > blue_threshold)
						retval++;
				}
			}
		}
	}
	return retval;
}

/* Anshuman : 16 Feb 2012 : determine on a block basis if the matrices differ from each other.
*  The threshold factor is the factor to be taken into consideration when deciding how many pixels have to be different 
*  for the images to be considered different 
*/
int block_pixel_differ(Mat& mat1, Mat& mat2, int block_size)
{
	/* Check conditions like rows and cols are not matching */
	if (!((mat1.rows == mat2.rows) && (mat1.cols == mat2.cols)))
		return  0;
	/* Check if the matrices are not 8 bit 3 channel images */
	if (mat1.type() != CV_8UC3)
		return 0;
	if (mat2.type() != CV_8UC3)
		return 0;
	/*The algorithm will divide the blocks into blocksize x blocksize squares
	* In most cases squares will not fit perfectly into the image matrix
	* We make a new matrix taking only pixel values for the center of the blocks
	* First we calculate the number of rows and columns in such a matrix.
	* The idea is that the last edge on rows and column side will have smaller squares
	*/
	
	int block_matrix_rows;
	int block_matrix_cols;

	if(mat1.rows % block_size  == 0)
		block_matrix_rows = mat1.rows/block_size;
	else {
		if (block_size > mat1.rows)
			block_matrix_rows = 1;
		else 
			block_matrix_rows = mat1.rows/block_size + 1;
	}

	if(mat1.cols % block_size  == 0)
		block_matrix_cols = mat1.cols/block_size;
	else {
		if (block_size > mat1.cols)
			block_matrix_cols = 1;
		else 
			block_matrix_cols = mat1.cols/block_size + 1;
	}


	Mat block_matrix_1(block_matrix_cols, block_matrix_rows, CV_8UC3);
	Mat block_matrix_2(block_matrix_cols, block_matrix_rows, CV_8UC3);

	/* Create the block matrix from the original images taking into account the center value of the 
	* pixel blocks in the original images
	*/
	int i;
	int j;
	/* calculate the value of the center pixel from original image to be taken as the pixel
	* value for the pixel value of the block matrix at 1,1
	*/
	int first_block_row_center = block_size/2;
	int first_block_col_center = block_size/2;
	for(i=0; i<block_matrix_rows; i++) {
		for(j=0; j<block_matrix_cols; j++) {
			/* The block center will move by block_size at each iteration rowwise and columnwise 
			*  If it falls beyond the edge of the image take the edge value 
			*/
			int curr_block_row_center = first_block_row_center + block_size * i;
			if (curr_block_row_center > mat1.rows)
				curr_block_row_center = mat1.rows - 1;
			int curr_block_col_center = first_block_col_center + block_size * j;
			if (curr_block_col_center > mat1.cols)
				curr_block_col_center = mat1.cols - 1;
			block_matrix_1.at<unsigned int>(i,j) = mat1.at<unsigned int>(curr_block_row_center, curr_block_col_center);
			block_matrix_2.at<unsigned int>(i,j) = mat2.at<unsigned int>(curr_block_row_center, curr_block_col_center);
		}
	}
	/* Now we calculate the number of differing pixels between the block matrices */
	int num_block_pixels_differ = pixel_differ(block_matrix_1, block_matrix_2);
	int num_pixels_threshold = (block_matrix_rows * block_matrix_cols * 3)/4;
	if (num_block_pixels_differ > num_pixels_threshold)
		return 1;
	return 0;
			
}


/* Anshuman : 19 Feb 2012 : added pixel differ algorithm based on color wise segmentation of a picture
* The basic idea is to segment a picture into color zones - identifying the amount of red, green and blue color in the picture 
* and then marking pixels as bordering towards red, green or blue and taking an aggregate count
* If these red, green and blue pixels differ by a threshold, we mark the images as different 
*/

int color_pixel_differ(Mat& mat1, Mat&mat2)
{
	/* Check conditions like rows and cols are not matching */
	if (!((mat1.rows == mat2.rows) && (mat1.cols == mat2.cols)))
		return  -1;
	/* Check if the matrices are not 8 bit 3 channel images */
	if (mat1.type() != CV_8UC3)
		return -1;
	if (mat2.type() != CV_8UC3)
		return -1;

	/* Split the matrices into three channels */
	std::vector<Mat> three_channels_mat1;
	cv::split(mat1, three_channels_mat1);
	std::vector<Mat> three_channels_mat2;
	cv::split(mat2, three_channels_mat2);
	/* Variables for holding the number of pixels bordering towards red, green and blue in the matrices */
	unsigned int pixels_red_mat1=0;
	unsigned int pixels_green_mat1=0;
	unsigned int pixels_blue_mat1=0;
	unsigned int pixels_red_mat2=0;
	unsigned int pixels_green_mat2=0;
	unsigned int pixels_blue_mat2=0;
	int i, j;
	for(i=0; i<mat1.rows; i++) {
		for(j=0; j<mat1.cols; j++) {
			
			/* Extract the channel values */
			uchar pixel_1_r = three_channels_mat1[2].at<uchar>(i,j);
			uchar pixel_1_g = three_channels_mat1[1].at<uchar>(i,j);
			uchar pixel_1_b = three_channels_mat1[0].at<uchar>(i,j);

			uchar pixel_2_r = three_channels_mat2[2].at<uchar>(i,j);
			uchar pixel_2_g = three_channels_mat2[1].at<uchar>(i,j);
			uchar pixel_2_b = three_channels_mat2[0].at<uchar>(i,j);
			
			/*Identify for each of the channels, which one is the max and then increment the appropriate counter */
			if(pixel_1_r >= pixel_1_g) {
				if (pixel_1_r >= pixel_1_b) {
					/* red is the maximum */
					pixels_red_mat1++;
				}
				else {
					/* blue is the maximum */
					pixels_blue_mat1++;
				}
			}
			else if (pixel_1_g >= pixel_1_b) {
				/* green is the maximum */
				pixels_green_mat1++;
			}
			else {
				/*blue is the maximum */
				pixels_blue_mat1++;
			}
			/*Identify for each of the channels, which one is the max and then increment the appropriate counter */
			if(pixel_2_r >= pixel_2_g) {
				if (pixel_2_r >= pixel_2_b) {
					/* red is the maximum */
					pixels_red_mat2++;
				}
				else {
					/* blue is the maximum */
					pixels_blue_mat2++;
				}
			}
			else if (pixel_2_g >= pixel_2_b) {
				/* green is the maximum */
				pixels_green_mat2++;
			}
			else {
				/*blue is the maximum */
				pixels_blue_mat2++;
			}
		}
	}
	/*Calculate pixel threshold values */
	unsigned int pixels_red_difference;
	unsigned int pixels_green_difference;
	unsigned int pixels_blue_difference;
	unsigned int pixels_threshold = (mat1.rows * mat1.cols) / 24;
	if (pixels_red_mat1 > pixels_red_mat2) {
		pixels_red_difference = pixels_red_mat1 - pixels_red_mat2;	
	}
	else
		pixels_red_difference = pixels_red_mat2 - pixels_red_mat1;
	if (pixels_green_mat1 > pixels_green_mat2) {
		pixels_green_difference = pixels_green_mat1 - pixels_green_mat2;	
	}
	else
		pixels_green_difference = pixels_green_mat2 - pixels_green_mat1;
	if (pixels_blue_mat1 > pixels_blue_mat2) {
		pixels_blue_difference = pixels_blue_mat1 - pixels_blue_mat2;	
	}
	else
		pixels_blue_difference = pixels_blue_mat2 - pixels_blue_mat1;
	/*
	cout << "Pixel rows " << mat1.rows << " cols " << mat1.cols << " in matrix 1 \n";
	cout << "Pixel threshold " << pixels_threshold << " \n";
	cout << "Pixel red in matrix 1 " << pixels_red_mat1 << "\n";
	cout << "Pixel red in matrix 2 " << pixels_red_mat2 << "\n";
	cout << "Pixel red difference  " << pixels_red_difference << "\n";
	cout << "Pixel green in matrix 1 " << pixels_green_mat1 << "\n";
	cout << "Pixel green in matrix 2 " << pixels_green_mat2 << "\n";
	cout << "Pixel green difference " << pixels_green_difference << "\n";
	cout << "Pixel blue in matrix 1 " << pixels_blue_mat1 << "\n";
	cout << "Pixel blue in matrix 2 " << pixels_blue_mat2 << "\n";
	cout << "Pixel blue difference " << pixels_blue_difference << "\n";
	*/
	if ((pixels_red_difference  + pixels_green_difference  + pixels_blue_difference) > pixels_threshold)
		return 1;
	
	return 0;
}



int main(int argc, char**argv)
{
	if (argc > 1) {
		unsigned int num_thumbnails=0;
		/*Load the video */
                CvCapture* video_capture_file = cvCaptureFromFile(argv[1]);
                if (video_capture_file == 0) {
                        cout << "Could not load Video \n";
                        return 1;
                }
		if (argc > 2) {
			/* Check if there was a limit on the number of thumbnails specified */
			num_thumbnails = atoi(argv[2]);
		}
			
		
                /*Initialize the index frame */
                IplImage* first_pass_index_frame = cvQueryFrame(video_capture_file);
                if(first_pass_index_frame != 0) {
                        Mat::Mat* first_pass_index_matrix = new Mat::Mat(first_pass_index_frame, true);
			/*First Pass Initialize the threshold for point of interest as 50% of the frame size */
			int pixels_difference_threshold_first_pass = (first_pass_index_matrix->rows * first_pass_index_matrix->cols )  /  2;
			/*Load the current frame */
                        IplImage* first_pass_current_frame = cvQueryFrame(video_capture_file);
			Mat::Mat* first_pass_current_matrix = new Mat::Mat(first_pass_current_frame, true);
			int current_frame_num = 1;
			/*Initialize pixel difference algorithm metrics */
			int num_pixels_different = 0 ;
			int first_pass_point_of_interest_frame_count = 0;
			int second_pass_point_of_interest_frame_count = 0;
			int third_pass_point_of_interest_frame_count = 0;
			char FirstPassPOIFileName[100];
			char SecondPassPOIFileName[100];
			char ThirdPassPOIFileName[100];
                        while(first_pass_current_frame != NULL) {
				first_pass_current_matrix = new Mat::Mat(first_pass_current_frame, true);
				/*Evaluate how many pixels are different */
				num_pixels_different = pixel_differ(*first_pass_index_matrix, *first_pass_current_matrix);
				if (num_pixels_different > pixels_difference_threshold_first_pass) {
					/* We have found a point of interest */
					first_pass_point_of_interest_frame_count++;
					/* Save the frame */
					//cout << "First Pass : Frame number " << current_frame_num << " is a point of interest  \n";	
					sprintf(FirstPassPOIFileName, "POI-FP-%d.jpeg", first_pass_point_of_interest_frame_count);
					imwrite(FirstPassPOIFileName, *first_pass_current_matrix);
					/* Reset index frame to current frame */	
					delete(first_pass_index_matrix);
					first_pass_index_matrix = new Mat::Mat(first_pass_current_frame, true);
				}
				/* Reset current matrix */
				delete(first_pass_current_matrix);
                        	first_pass_current_frame = cvQueryFrame(video_capture_file);
				current_frame_num++;
			}
			//cout << "First Pass Done \n";
			//cout << "Begin Second Pass \n";
			/* Begin second pass */
			int i=1;
			/* Data structures for second pass index and current frames */
			/* For the second pass now we use a block based algorithm */
                        IplImage* second_pass_index_frame;
                        IplImage* second_pass_current_frame;
			Mat::Mat* second_pass_index_matrix;
			Mat::Mat* second_pass_current_matrix;
			if (first_pass_point_of_interest_frame_count > 1) {
				/* Load the index frame */
				sprintf(FirstPassPOIFileName, "POI-FP-%d.jpeg", i);
				second_pass_index_frame = cvLoadImage(FirstPassPOIFileName);
				remove(FirstPassPOIFileName);
				second_pass_index_matrix = new Mat::Mat(second_pass_index_frame, true);
				/* Iterate over the frames and detect similar  */
				for(i=2; i<=first_pass_point_of_interest_frame_count; i++) {
					sprintf(FirstPassPOIFileName, "POI-FP-%d.jpeg", i);
					second_pass_current_frame = cvLoadImage(FirstPassPOIFileName);
					second_pass_current_matrix = new Mat::Mat(second_pass_current_frame, true);
					if (block_pixel_differ(*second_pass_index_matrix, *second_pass_current_matrix, 24)) {
						/* We have found a point of interest */
						second_pass_point_of_interest_frame_count++;
						/* Save the frame  */
						cout << "Second Pass : Frame number " << i << " is a point of interest  \n";	
						sprintf(SecondPassPOIFileName, "POI-SP-%d.jpeg", second_pass_point_of_interest_frame_count);
						imwrite(SecondPassPOIFileName, *second_pass_current_matrix);
						/* Reset index frame to current frame */	
						delete(second_pass_index_matrix);
						second_pass_index_matrix = new Mat::Mat(second_pass_current_frame, true);
					}
					/* Reset current matrix */
					delete(second_pass_current_matrix);
					remove(FirstPassPOIFileName);
				}	
			}
			//cout << "Begin Third Pass \n";
			/* Begin third pass */
			/* Data structures for second pass index and current frames */
			/* For the third pass now we use a color based algorithm */
                        IplImage* third_pass_index_frame;
                        IplImage* third_pass_current_frame;
			Mat::Mat* third_pass_index_matrix;
			Mat::Mat* third_pass_current_matrix;
			if (second_pass_point_of_interest_frame_count > 1) {
				/* Load the index frame */
				i=1;
				sprintf(SecondPassPOIFileName, "POI-SP-%d.jpeg", i);
				third_pass_index_frame = cvLoadImage(SecondPassPOIFileName);
				remove(SecondPassPOIFileName);
				third_pass_index_matrix = new Mat::Mat(third_pass_index_frame, true);
				/* Iterate over the frames and detect similar  */
				for(i=2; i<=second_pass_point_of_interest_frame_count; i++) {
					sprintf(SecondPassPOIFileName, "POI-SP-%d.jpeg", i);
					third_pass_current_frame = cvLoadImage(SecondPassPOIFileName);
					third_pass_current_matrix = new Mat::Mat(third_pass_current_frame, true);
					if (color_pixel_differ(*third_pass_index_matrix, *third_pass_current_matrix)) {
						/* We have found a point of interest */
						third_pass_point_of_interest_frame_count++;
						/* Save the frame  */
						cout << "Third Pass : Frame number " << i << " is a point of interest  \n";	
						sprintf(ThirdPassPOIFileName, "POI-TP-%d.jpeg", third_pass_point_of_interest_frame_count);
						imwrite(ThirdPassPOIFileName, *third_pass_current_matrix);
						/* Reset index frame to current frame */	
						delete(third_pass_index_matrix);
						third_pass_index_matrix = new Mat::Mat(third_pass_current_frame, true);
					}
					/* Reset current matrix */
					delete(third_pass_current_matrix);
					remove(SecondPassPOIFileName);
				}	
			}
			cout << "Third Pass Done";
			FILE *fp=fopen("algo.out", "w");
			fprintf(fp, "%d\n", third_pass_point_of_interest_frame_count);
			fclose(fp);
			return 0;
        	}
		else {
			cout << "Could not extract first index frame from video \n";
			return 1;
		}
	}
	cout << "Please give a video filename \n";
	return 1;
}

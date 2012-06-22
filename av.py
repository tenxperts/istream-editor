from ctypes import *

_libraries = {}
_libraries['/usr/local/lib/libavcodec.so'] = CDLL('/usr/local/lib/libavcodec.so')
STRING = c_char_p
_libraries['/usr/local/lib/libavdevice.so'] = CDLL('/usr/local/lib/libavdevice.so')
_libraries['/usr/local/lib/libavformat.so'] = CDLL('/usr/local/lib/libavformat.so')
_libraries['/usr/local/lib/libswscale.so'] = CDLL('/usr/local/lib/libswscale.so')
WSTRING = c_wchar_p


def WIFEXITED(status): return __WIFEXITED (__WAIT_INT (status)) # macro
AV_ROUND_NEAR_INF = 5
_POSIX_THREAD_DESTRUCTOR_ITERATIONS = 4 # Variable c_int '4'
PTHREAD_DESTRUCTOR_ITERATIONS = _POSIX_THREAD_DESTRUCTOR_ITERATIONS # alias
__PDP_ENDIAN = 3412 # Variable c_int '3412'
PDP_ENDIAN = __PDP_ENDIAN # alias
# def __bswap_16(x): return (__extension__ ({ register unsigned short int __v, __x = (unsigned short int) (x); if (__builtin_constant_p (__x)) __v = __bswap_constant_16 (__x); else __asm__ ("rorw $8, %w0" : "=r" (__v) : "0" (__x) : "cc"); __v; })) # macro
_ISspace = 8192
AV_ROUND_ZERO = 0
def WIFCONTINUED(status): return __WIFCONTINUED (__WAIT_INT (status)) # macro
PIX_FMT_GRAY8A = 66
PIX_FMT_Y400A = PIX_FMT_GRAY8A # alias
PIX_FMT_YUV444P9LE = 76
CODEC_ID_PAM = 68
_ISxdigit = 4096
_POSIX2_BC_SCALE_MAX = 99 # Variable c_int '99'
BC_SCALE_MAX = _POSIX2_BC_SCALE_MAX # alias
_POSIX2_BC_BASE_MAX = 99 # Variable c_int '99'
BC_BASE_MAX = _POSIX2_BC_BASE_MAX # alias
AVMEDIA_TYPE_NB = 5
AVMEDIA_TYPE_SUBTITLE = 3
AVMEDIA_TYPE_DATA = 2
CODEC_ID_WMAV2 = 86024
AVSTREAM_PARSE_FULL_ONCE = 4
AVMEDIA_TYPE_AUDIO = 1
# __RLIM_T_TYPE = __ULONGWORD_TYPE # alias
# av_log2 = av_log2_c # alias
AV_PKT_DATA_NEW_EXTRADATA = 1
CODEC_ID_G729 = 86070
def UINTMAX_C(c): return c ## UL # macro
def va_start(v,l): return __builtin_va_start(v,l) # macro
def va_copy(d,s): return __builtin_va_copy(d,s) # macro
def va_arg(v,l): return __builtin_va_arg(v,l) # macro
AVCHROMA_LOC_BOTTOMLEFT = 5
def toascii_l(c,l): return __toascii_l ((c), (l)) # macro
AVCHROMA_LOC_CENTER = 2
def makedev(maj,min): return gnu_dev_makedev (maj, min) # macro
def le32toh(x): return (x) # macro
def le16toh(x): return (x) # macro
PIX_FMT_YUV444P9BE = 75
def UINT8_C(c): return c # macro
FP_SUBNORMAL = 3
CODEC_ID_XBIN = 1480739150
CODEC_ID_DVAUDIO = 86022
AVCOL_PRI_BT470M = 4
__codecvt_noconv = 3
# __S32_TYPE = int # alias
# __PID_T_TYPE = __S32_TYPE # alias
__codecvt_error = 2
_ISlower = 512
ME_ITER = 9
AVCOL_SPC_BT709 = 1
CODEC_ID_BMP = 80
PIX_FMT_YUV422P10LE = 74
PIX_FMT_BGR555BE = 49
CODEC_ID_R10K = 147
def __attribute_format_arg__(x): return __attribute__ ((__format_arg__ (x))) # macro
# __OFF_T_TYPE = __SLONGWORD_TYPE # alias
ME_UMH = 8
def isupper_l(c,l): return __isupper_l ((c), (l)) # macro
def isunordered(u,v): return __builtin_isunordered(u, v) # macro
AV_LOCK_RELEASE = 2
def isspace_l(c,l): return __isspace_l ((c), (l)) # macro
AV_LOCK_CREATE = 0
CODEC_ID_DTS = 86020
def ispunct_l(c,l): return __ispunct_l ((c), (l)) # macro
CODEC_ID_PGMYUV = 67
def isnormal(x): return (fpclassify (x) == FP_NORMAL) # macro
# def isnan(x): return (sizeof (x) == sizeof (float) ? __isnanf (x) : sizeof (x) == sizeof (double) ? __isnan (x) : __isnanl (x)) # macro
AV_ROUND_INF = 1
def islower_l(c,l): return __islower_l ((c), (l)) # macro
AVSTREAM_PARSE_FULL_RAW = 1463898624
def islessgreater(x,y): return __builtin_islessgreater(x, y) # macro
def islessequal(x,y): return __builtin_islessequal(x, y) # macro
ME_HEX = 7
def isless(x,y): return __builtin_isless(x, y) # macro
# def isinf(x): return (sizeof (x) == sizeof (float) ? __isinff (x) : sizeof (x) == sizeof (double) ? __isinf (x) : __isinfl (x)) # macro
def isgreaterequal(x,y): return __builtin_isgreaterequal(x, y) # macro
PIX_FMT_YUV444P = 5
def isgreater(x,y): return __builtin_isgreater(x, y) # macro
def isgraph_l(c,l): return __isgraph_l ((c), (l)) # macro
CODEC_ID_FRAPS = 78
# def isfinite(x): return (sizeof (x) == sizeof (float) ? __finitef (x) : sizeof (x) == sizeof (double) ? __finite (x) : __finitel (x)) # macro
def isdigit_l(c,l): return __isdigit_l ((c), (l)) # macro
PIX_FMT_YUV420P10LE = 72
def iscntrl_l(c,l): return __iscntrl_l ((c), (l)) # macro
SUBTITLE_ASS = 3
CODEC_ID_A64_MULTI = 145
def isblank_l(c,l): return __isblank_l ((c), (l)) # macro
AVSTREAM_PARSE_HEADERS = 2
def isalpha_l(c,l): return __isalpha_l ((c), (l)) # macro
def htole64(x): return (x) # macro
def htole32(x): return (x) # macro
def htole16(x): return (x) # macro
def htobe16(x): return __bswap_16 (x) # macro
# def fpclassify(x): return (sizeof (x) == sizeof (float) ? __fpclassifyf (x) : sizeof (x) == sizeof (double) ? __fpclassify (x) : __fpclassifyl (x)) # macro
def be64toh(x): return __bswap_64 (x) # macro
def be32toh(x): return __bswap_32 (x) # macro
# av_extern_inline = inline # alias
# def av_uninit(x): return x=x # macro
def av_printf_format(fmtpos,attrpos): return __attribute__((__format__(__printf__, fmtpos, attrpos))) # macro
def av_alloc_size(n): return __attribute__((alloc_size(n))) # macro
# def __warndecl(name,msg): return extern void name (void) __attribute__((__warning__ (msg))) # macro
def __warnattr(msg): return __attribute__((__warning__ (msg))) # macro
CODEC_ID_ADPCM_IMA_EA_SEAD = 69655
def __va_copy(d,s): return __builtin_va_copy(d,s) # macro
CODEC_ID_ANSI = 144
CODEC_ID_AAC = 86018
# INT_MAX = __INT_MAX__ # alias
# NL_MSGMAX = INT_MAX # alias
def __W_EXITCODE(ret,sig): return ((ret) << 8 | (sig)) # macro
# __MODE_T_TYPE = __U32_TYPE # alias
ME_EPZS = 5
AV_MATRIX_ENCODING_DPLII = 2
AVCOL_PRI_UNSPECIFIED = 2
AV_FIELD_BT = 5
# __MATH_INLINE = __extern_inline # alias
AV_PKT_DATA_PARAM_CHANGE = 2
CODEC_ID_ADPCM_SBPRO_4 = 69647
# def __nonnull(params): return __attribute__ ((__nonnull__ params)) # macro
def __CONCAT(x,y): return x ## y # macro
CODEC_ID_ADPCM_YAMAHA = 69646
CODEC_ID_WNV1 = 75
AVCOL_RANGE_NB = 3
AVCOL_RANGE_MPEG = 1
CODEC_ID_ADPCM_SWF = 69645
PIX_FMT_BGR565LE = 48
# def PUT_UTF8(val,tmp,PUT_BYTE): return { int bytes, shift; uint32_t in = val; if (in < 0x80) { tmp = in; PUT_BYTE } else { bytes = (av_log2(in) + 4) / 5; shift = (bytes - 1) * 6; tmp = (256 - (256 >> bytes)) | (in >> shift); PUT_BYTE while (shift >= 6) { shift -= 6; tmp = 0x80 | ((in >> shift) & 0x3f); PUT_BYTE } } } # macro
CODEC_ID_ADPCM_CT = 69644
def __isspace_l(c,l): return __isctype_l((c), _ISspace, (l)) # macro
# NL_TEXTMAX = INT_MAX # alias
PIX_FMT_BGR0 = 298
CODEC_ID_ADPCM_EA = 69642
ME_LOG = 3
def __isprint_l(c,l): return __isctype_l((c), _ISprint, (l)) # macro
AV_AUDIO_SERVICE_TYPE_EMERGENCY = 6
CODEC_ID_ADPCM_ADX = 69641
CODEC_ID_ADPCM_XA = 69640
PIX_FMT_BGRA64LE = 294
AVCOL_PRI_SMPTE240M = 7
__NFDBITS = 64 # Variable c_int '64'
NFDBITS = __NFDBITS # alias
PIX_FMT_BGRA64BE = 293
PIX_FMT_RGBA64LE = 292
ME_FULL = 2
CODEC_ID_MPEG4SYSTEMS = 131073
# _IO_HAVE_ST_BLKSIZE = _G_HAVE_ST_BLKSIZE # alias
# def __isctype(c,type): return ((*__ctype_b_loc ())[(int) (c)] & (unsigned short int) type) # macro
PIX_FMT_GBRP16LE = 88
def __iscntrl_l(c,l): return __isctype_l((c), _IScntrl, (l)) # macro
PIX_FMT_GBRP16BE = 87
def __isblank_l(c,l): return __isctype_l((c), _ISblank, (l)) # macro
class _IO_FILE(Structure):
    pass
stdout = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'stdout')
stdout = stdout # alias
# def __u_intN_t(N,MODE): return typedef unsigned int u_int ##N ##_t __attribute__ ((__mode__ (MODE))) # macro
# def __tobody(c,f,a,args): return (__extension__ ({ int __res; if (sizeof (c) > 1) { if (__builtin_constant_p (c)) { int __c = (c); __res = __c < -128 || __c > 255 ? __c : (a)[__c]; } else __res = f args; } else __res = (a)[(int) (c)]; __res; })) # macro
def __toascii_l(c,l): return ((l), __toascii (c)) # macro
CODEC_ID_ADPCM_IMA_QT = 69632
AVLINK_STARTINIT = 1
def __isxdigit_l(c,l): return __isctype_l((c), _ISxdigit, (l)) # macro
# av_clipl_int32 = av_clipl_int32_c # alias
def __isupper_l(c,l): return __isctype_l((c), _ISupper, (l)) # macro
def __ispunct_l(c,l): return __isctype_l((c), _ISpunct, (l)) # macro
CODEC_ID_PCM_S8_PLANAR = 65563
def __islower_l(c,l): return __isctype_l((c), _ISlower, (l)) # macro
def __isascii(c): return (((c) & ~0x7f) == 0) # macro
# def __isleap(year): return ((year) % 4 == 0 && ((year) % 100 != 0 || (year) % 400 == 0)) # macro
def __isgraph_l(c,l): return __isctype_l((c), _ISgraph, (l)) # macro
CODEC_ID_FFMETADATA = 135168
# av_restrict = restrict # alias
CODEC_ID_PROBE = 102400
CODEC_ID_IDF = 4801606
CODEC_ID_BINTEXT = 1112823892
CODEC_ID_TTF = 98304
# av_popcount64 = av_popcount64_c # alias
CODEC_ID_FIRST_UNKNOWN = 98304
CODEC_ID_JACOSUB = 1246975298
CODEC_ID_EIA_608 = 1664495672
# def __intN_t(N,MODE): return typedef int int ##N ##_t __attribute__ ((__mode__ (MODE))) # macro
# LONG_LONG_MAX = __LONG_LONG_MAX__ # alias
CODEC_ID_SRT = 94216
CODEC_ID_DVB_TELETEXT = 94215
# av_popcount = av_popcount_c # alias
CODEC_ID_HDMV_PGS_SUBTITLE = 94214
CODEC_ID_SSA = 94212
CODEC_ID_XSUB = 94211
# def __bswap_32(x): return (__extension__ ({ register unsigned int __v, __x = (x); if (__builtin_constant_p (__x)) __v = __bswap_constant_32 (__x); else __asm__ ("bswap %0" : "=r" (__v) : "0" (__x)); __v; })) # macro
CODEC_ID_FIRST_SUBTITLE = 94208
CODEC_ID_SONIC_LS = 1397706316
CODEC_ID_FFWAVESYNTH = 1179014995
# def __exctype_l(name): return extern int name (int, __locale_t) __THROW # macro
def __WTERMSIG(status): return ((status) & 0x7f) # macro
def __WSTOPSIG(status): return __WEXITSTATUS(status) # macro
CODEC_ID_8SVX_EXP = 86071
# def FFERRTAG(a,b,c,d): return (-(int)MKTAG(a, b, c, d)) # macro
CODEC_ID_G723_1 = 86069
CODEC_ID_CELT = 86068
def MKBETAG(a,b,c,d): return ((d) | ((c) << 8) | ((b) << 16) | ((unsigned)(a) << 24)) # macro
def __WIFEXITED(status): return (__WTERMSIG(status) == 0) # macro
CODEC_ID_AAC_LATM = 86066
CODEC_ID_BINKAUDIO_DCT = 86065
CODEC_ID_PCM_F32BE = 65556
CODEC_ID_BINKAUDIO_RDFT = 86064
# def __errordecl(name,msg): return extern void name (void) __attribute__((__error__ (msg))) # macro
CODEC_ID_ROQ_DPCM = 81920
def __WEXITSTATUS(status): return (((status) & 0xff00) >> 8) # macro
CODEC_ID_TWINVQ = 86060
# def __WAIT_INT(status): return (*(int *) &(status)) # macro
CODEC_ID_MOV_TEXT = 94213
def __REDIRECT_NTH_LDBL(name,proto,alias): return __REDIRECT_NTH (name, proto, alias) # macro
CODEC_ID_PCM_S16LE_PLANAR = 65554
# av_clip_uint8 = av_clip_uint8_c # alias
PIX_FMT_BGR444BE = 65
# av_clip_uint16 = av_clip_uint16_c # alias
# def strndupa(s,n): return (__extension__ ({ __const char *__old = (s); size_t __len = strnlen (__old, (n)); char *__new = (char *) __builtin_alloca (__len + 1); __new[__len] = '\0'; (char *) memcpy (__new, __old, __len); })) # macro
CODEC_ID_DVB_SUBTITLE = 94209
__LITTLE_ENDIAN = 1234 # Variable c_int '1234'
LITTLE_ENDIAN = __LITTLE_ENDIAN # alias
AVMEDIA_TYPE_ATTACHMENT = 4
# __FSFILCNT_T_TYPE = __ULONGWORD_TYPE # alias
AVCOL_TRC_NB = 8
AVCOL_TRC_SMPTE240M = 7
AVCOL_TRC_UNSPECIFIED = 2
# av_ceil_log2 = av_ceil_log2_c # alias
def __bos(ptr): return __builtin_object_size (ptr, __USE_FORTIFY_LEVEL > 1) # macro
PIX_FMT_BGR444LE = 64
def __attribute_format_strfmon__(a,b): return __attribute__ ((__format__ (__strfmon__, a, b))) # macro
CODEC_ID_PCM_U32LE = 65546
AVMEDIA_TYPE_VIDEO = 0
CODEC_ID_RA_144 = 77824
PIX_FMT_YUV422P10BE = 73
def __W_STOPCODE(sig): return ((sig) << 8 | 0x7f) # macro
# def __REDIRECT_NTH(name,proto,alias): return name proto __THROW __asm__ (__ASMNAME (#alias)) # macro
def __REDIRECT_LDBL(name,proto,alias): return __REDIRECT (name, proto, alias) # macro
# def __REDIRECT(name,proto,alias): return name proto __asm__ (__ASMNAME (#alias)) # macro
def __PMT(args): return args # macro
CODEC_ID_WMALOSSLESS = 86055
def __P(args): return args # macro
# def __NTH(fct): return fct throw () # macro
AV_PICTURE_TYPE_S = 4
PIX_FMT_RGB444BE = 63
CODEC_ID_WMAPRO = 86054
# def __LDBL_REDIR1(name,proto,alias): return name proto # macro
# def __LDBL_REDIR(name,proto): return name proto # macro
# def __FD_ZERO(fdsp): return do { int __d0, __d1; __asm__ __volatile__ ("cld; rep; " __FD_ZERO_STOS : "=c" (__d0), "=D" (__d1) : "a" (0), "0" (sizeof (fd_set) / sizeof (__fd_mask)), "1" (&__FDS_BITS (fdsp)[0]) : "memory"); } while (0) # macro
CODEC_ID_WMAVOICE = 86053
# def GET_UTF16(val,GET_16BIT,ERROR): return val = GET_16BIT; { unsigned int hi = val - 0xD800; if (hi < 0x800) { val = GET_16BIT - 0xDC00; if (val > 0x3FFU || hi > 0x3FFU) ERROR val += (hi<<10) + 0x10000; } } # macro
AV_PICTURE_TYPE_P = 2
# def __FD_CLR(d,set): return ((void) (__FDS_BITS (set)[__FDELT (d)] &= ~__FDMASK (d))) # macro
CODEC_ID_SPEEX = 86052
AV_PICTURE_TYPE_I = 1
# def __ASMNAME2(prefix,cname): return __STRING (prefix) cname # macro
def __ASMNAME(cname): return __ASMNAME2 (__USER_LABEL_PREFIX__, cname) # macro
def _PARAMS(protos): return __P(protos) # macro
# def _ISbit(bit): return ((bit) < 8 ? ((1 << (bit)) << 8) : ((1 << (bit)) >> 8)) # macro
CODEC_ID_MUSEPACK8 = 86051
# def _IO_putc_unlocked(_ch,_fp): return (_IO_BE ((_fp)->_IO_write_ptr >= (_fp)->_IO_write_end, 0) ? __overflow (_fp, (unsigned char) (_ch)) : (unsigned char) (*(_fp)->_IO_write_ptr++ = (_ch))) # macro
def _IO_peekc(_fp): return _IO_peekc_unlocked (_fp) # macro
CODEC_ID_NELLYMOSER = 86050
AVLINK_INIT = 2
PIX_FMT_RGB444LE = 62
CODEC_ID_ATRAC3 = 86047
def WIFSTOPPED(status): return __WIFSTOPPED (__WAIT_INT (status)) # macro
def INT32_C(c): return c # macro
def UINT32_C(c): return c ## U # macro
def UINT16_C(c): return c # macro
# def RSHIFT(a,b): return ((a) > 0 ? ((a) + ((1<<(b))>>1))>>(b) : ((a) + ((1<<(b))>>1)-1)>>(b)) # macro
# def PUT_UTF16(val,tmp,PUT_16BIT): return { uint32_t in = val; if (in < 0x10000) { tmp = in; PUT_16BIT } else { tmp = 0xD800 | ((in - 0x10000) >> 10); PUT_16BIT tmp = 0xDC00 | ((in - 0x10000) & 0x3FF); PUT_16BIT } } # macro
def PIX_FMT_NE(be,le): return PIX_FMT_ ##le # macro
def MKTAG(a,b,c,d): return ((a) | ((b) << 8) | ((c) << 16) | ((unsigned)(d) << 24)) # macro
def INTMAX_C(c): return c ## L # macro
def INT8_C(c): return c # macro
def FFALIGN(x,a): return (((x)+(a)-1)&~((a)-1)) # macro
CODEC_ID_PGM = 66
# def FFABS(a): return ((a) >= 0 ? (a) : (-(a))) # macro
_SVID_ = 0
PIX_FMT_DXVA2_VLD = 61
def FD_ZERO(fdsetp): return __FD_ZERO (fdsetp) # macro
CODEC_ID_MUSEPACK7 = 86044
ME_TESA = 10
def __WIFCONTINUED(status): return ((status) == __W_CONTINUED) # macro
def FD_ISSET(fd,fdsetp): return __FD_ISSET (fd, fdsetp) # macro
CODEC_ID_ATRAC1 = 86063
def AV_VERSION(a,b,c): return AV_VERSION_DOT(a, b, c) # macro
PIX_FMT_VAAPI_IDCT = 52
AV_FIELD_TB = 4
CODEC_ID_WAVPACK = 86041
def AV_JOIN(a,b): return AV_GLUE(a, b) # macro
def AV_GLUE(a,b): return a ## b # macro
CODEC_ID_TRUEHD = 86061
def AVUNERROR(e): return (-(e)) # macro
CODEC_ID_QCELP = 86040
CODEC_ID_PBM = 65
PIX_FMT_VDPAU_MPEG4 = 60
CODEC_ID_MP1 = 86059
CODEC_ID_SIPR = 86058
# NL_NMAX = INT_MAX # alias
CODEC_ID_TRUESPEECH = 86037
CODEC_ID_EAC3 = 86057
PIX_FMT_RGB555LE = 46
CODEC_ID_PPM = 64
PIX_FMT_YUV444P16BE = 59
CODEC_ID_GSM = 86034
def htobe32(x): return __bswap_32 (x) # macro
AV_PKT_DATA_H263_MB_INFO = 3
AVMEDIA_TYPE_UNKNOWN = -1
CODEC_ID_ALAC = 86032
def __WCOREDUMP(status): return ((status) & __WCOREFLAG) # macro
AVCOL_SPC_SMPTE170M = 6
PIX_FMT_YUV444P16LE = 58
CODEC_ID_DPX = 130
CODEC_ID_QDMC = 86067
CODEC_ID_FLAC = 86028
PIX_FMT_VDPAU_MPEG1 = 37
CODEC_ID_MAD = 131
CODEC_ID_PCM_LXF = 65561
# __DEV_T_TYPE = __UQUAD_TYPE # alias
AVCHROMA_LOC_TOPLEFT = 3
# __DADDR_T_TYPE = __S32_TYPE # alias
PIX_FMT_YUV422P16BE = 57
PIX_FMT_YUV440P = 33
__BYTE_ORDER = __LITTLE_ENDIAN # alias
CODEC_ID_MICRODVD = 1833195076
PIX_FMT_BGRA = 30
PIX_FMT_YUV422P16LE = 56
PIX_FMT_ABGR = 29
_POSIX_UIO_MAXIOV = 16 # Variable c_int '16'
_XOPEN_IOV_MAX = _POSIX_UIO_MAXIOV # alias
PIX_FMT_ARGB = 27
def le64toh(x): return (x) # macro
PIX_FMT_NV21 = 26
AV_ROUND_UP = 3
PIX_FMT_NV12 = 25
CODEC_ID_XAN_DPCM = 81922
PIX_FMT_RGB555BE = 45
AV_SIDE_DATA_PARAM_CHANGE_DIMENSIONS = 8
AV_SIDE_DATA_PARAM_CHANGE_SAMPLE_RATE = 4
AV_SIDE_DATA_PARAM_CHANGE_CHANNEL_LAYOUT = 2
AV_SIDE_DATA_PARAM_CHANGE_CHANNEL_COUNT = 1
class __va_list_tag(Structure):
    pass
__va_list_tag._fields_ = [
]
__gnuc_va_list = __va_list_tag * 1
_IO_va_list = __gnuc_va_list # alias
AVCHROMA_LOC_TOP = 4
CODEC_ID_APE = 86049
CODEC_ID_VOXWARE = 86048
def __STRING(x): return #x # macro
CODEC_ID_GSM_MS = 86046
# __BLKSIZE_T_TYPE = __SLONGWORD_TYPE # alias
CODEC_ID_RA_288 = 77825
CODEC_ID_TTA = 86038
size_t = c_ulong
_G_size_t = size_t # alias
_IO_size_t = _G_size_t # alias
CODEC_ID_COOK = 86036
CODEC_ID_QDM2 = 86035
CODEC_ID_WESTWOOD_SND1 = 86033
PIX_FMT_YUV420P16LE = 54
ME_X1 = 6
PIX_FMT_BGR8 = 19
CODEC_ID_SHORTEN = 86031
CODEC_ID_VMDAUDIO = 86027
CODEC_ID_MACE6 = 86026
__pid_t = c_int
_G_pid_t = __pid_t # alias
_IO_pid_t = _G_pid_t # alias
CODEC_ID_MACE3 = 86025
CODEC_ID_WMAV1 = 86023
CODEC_ID_VORBIS = 86021
PIX_FMT_UYVY422 = 17
CODEC_ID_AC3 = 86019
CODEC_ID_MP3 = 86017
CODEC_ID_MP2 = 86016
CODEC_ID_SOL_DPCM = 81923
CODEC_ID_ADPCM_IMA_APC = 69661
CODEC_ID_INTERPLAY_DPCM = 81921
AVCOL_SPC_BT470BG = 5
CODEC_ID_AMR_WB = 73729
CODEC_ID_AMR_NB = 73728
CODEC_ID_VIMA = 1447644481
PIX_FMT_GRAY16BE = 31
CODEC_ID_ADPCM_G722 = 69660
CODEC_ID_ADPCM_IMA_ISS = 69659
PIX_FMT_VAAPI_VLD = 53
PIX_FMT_YUVJ444P = 14
CODEC_ID_PCM_S32LE = 65544
CODEC_ID_PCM_ALAW = 65543
# _IO_file_flags = _flags # alias
CODEC_ID_PCM_MULAW = 65542
CODEC_ID_PCM_U16BE = 65539
CODEC_ID_PCM_U16LE = 65538
AVDISCARD_ALL = 48
AVDISCARD_NONKEY = 32
CODEC_ID_SANM = 1396788813
AVDISCARD_NONREF = 8
CODEC_ID_V408 = 1446260792
CODEC_ID_V308 = 1446195256
AV_PKT_DATA_PALETTE = 0
AVCOL_TRC_GAMMA28 = 5
CODEC_ID_AVRP = 1096176208
CODEC_ID_EXR = 809850962
PIX_FMT_MONOWHITE = 9
# def __isctype_l(c,type,locale): return ((locale)->__ctype_b[(int) (c)] & (unsigned short int) type) # macro
CODEC_ID_MSS1 = 164
AVCOL_TRC_GAMMA22 = 4
CODEC_ID_ZEROCODEC = 163
CODEC_ID_XBM = 162
CODEC_ID_XWD = 160
PIX_FMT_GRAY8 = 8
CODEC_ID_DXTORY = 158
CODEC_ID_VBLE = 157
CODEC_ID_BMV_VIDEO = 156
CODEC_ID_VC1IMAGE = 154
CODEC_ID_WMV3IMAGE = 153
CODEC_ID_DFA = 152
AVCOL_TRC_BT709 = 1
CODEC_ID_JV = 151
CODEC_ID_PRORES = 150
CODEC_ID_LAGARITH = 149
CODEC_ID_MXPEG = 148
_G_va_list = __gnuc_va_list # alias
CODEC_ID_A64_MULTI5 = 146
CODEC_ID_PICTOR = 143
CODEC_ID_VP8 = 142
CODEC_ID_YOP = 141
CODEC_ID_IFF_ILBM = 138
CODEC_ID_BINKVIDEO = 137
FP_INFINITE = 1
FP_INFINITE = FP_INFINITE # alias
CODEC_ID_ANM = 136
# _G_stat64 = stat64 # alias
CODEC_ID_R210 = 135
CODEC_ID_CDGRAPHICS = 134
CODEC_ID_FLASHSV2 = 133
CODEC_ID_FRWU = 132
__ssize_t = c_long
_G_ssize_t = __ssize_t # alias
CODEC_ID_V210X = 127
CODEC_ID_TQI = 124
CODEC_ID_TGQ = 123
def va_end(v): return __builtin_va_end(v) # macro
CODEC_ID_MOTIONPIXELS = 121
__codecvt_ok = 0
CODEC_ID_CMV = 120
_ISalnum = 8
CODEC_ID_ESCAPE124 = 117
_IScntrl = 2
_ISblank = 1
_ISgraph = 32768
CODEC_ID_INDEO4 = 113
CODEC_ID_PCX = 111
_ISalpha = 1024
PIX_FMT_BGR555LE = 50
CODEC_ID_TXD = 107
__off_t = c_long
_G_off_t = __off_t # alias
CODEC_ID_PTX = 106
CODEC_ID_BETHSOFTVID = 105
CODEC_ID_THP = 102
CODEC_ID_DNXHD = 101
CODEC_ID_PCM_U8 = 65541
CODEC_ID_GIF = 99
CODEC_ID_TIFF = 98
CODEC_ID_TIERTEXSEQVIDEO = 97
CODEC_ID_DSICINVIDEO = 96
CODEC_ID_TARGA = 95
CODEC_ID_PCM_S8 = 65540
CODEC_ID_VP6 = 93
CODEC_ID_VP5 = 92
CODEC_ID_VMNC = 91
CODEC_ID_JPEG2000 = 90
CODEC_ID_CAVS = 89
CODEC_ID_FLASHSV = 88
CODEC_ID_KMVC = 87
CODEC_ID_NUV = 86
CODEC_ID_AVS = 84
CODEC_ID_ZMBV = 83
# _G_OPEN64 = __open64 # alias
CODEC_ID_MMVIDEO = 82
CODEC_ID_PCM_S16BE = 65537
CODEC_ID_AASC = 76
CODEC_ID_LOCO = 74
CODEC_ID_WMV3 = 73
CODEC_ID_RV40 = 71
CODEC_ID_PCM_S16LE = 65536
CODEC_ID_FFVHUFF = 69
def __MATHCALLX(function,suffix,args,attrib): return __MATHDECLX (_Mdouble_,function,suffix, args, attrib) # macro
AV_SAMPLE_FMT_S32P = 7
AV_SAMPLE_FMT_DBL = 4
AV_SAMPLE_FMT_FLT = 3
AVFILTER_PLANAR = 1
AV_SAMPLE_FMT_S32 = 2
CODEC_ID_QDRAW = 60
CODEC_ID_ULTI = 59
CODEC_ID_TSCC = 58
AVCOL_SPC_FCC = 4
CODEC_ID_SNOW = 57
CODEC_ID_QTRLE = 56
CODEC_ID_ZLIB = 55
CODEC_ID_MSZH = 54
CODEC_ID_YUV4 = 1498764852
CODEC_ID_VMDVIDEO = 53
CODEC_ID_TRUEMOTION1 = 52
CODEC_ID_FLIC = 51
CODEC_ID_8BPS = 49
CODEC_ID_IDCIN = 48
CODEC_ID_MSVIDEO1 = 47
CODEC_ID_MSRLE = 46
AVCHROMA_LOC_LEFT = 1
CODEC_ID_WS_VQA = 45
CODEC_ID_CINEPAK = 44
SUBTITLE_TEXT = 2
CODEC_ID_RPZA = 43
CODEC_ID_XAN_WC3 = 41
CODEC_ID_INTERPLAY_VIDEO = 40
def __LONG_LONG_PAIR(HI,LO): return LO, HI # macro
CODEC_ID_MDEC = 38
CODEC_ID_CLJR = 37
CODEC_ID_VCR1 = 36
CODEC_ID_AYUV = 1096373590
CODEC_ID_DVD_SUBTITLE = 94208
CODEC_ID_ASV2 = 33
# _G_wint_t = wint_t # alias
# _IO_wint_t = _G_wint_t # alias
CODEC_ID_THEORA = 31
CODEC_ID_VP3 = 30
CODEC_ID_H264 = 28
CODEC_ID_CYUV = 27
def __va_arg_pack(): return __builtin_va_arg_pack () # macro
CODEC_ID_HUFFYUV = 26
CODEC_ID_DVVIDEO = 25
CODEC_ID_SVQ3 = 24
CODEC_ID_SVQ1 = 23
CODEC_ID_FLV1 = 22
CODEC_ID_H263I = 21
CODEC_ID_H263P = 20
CODEC_ID_WMV2 = 19
CODEC_ID_WMV1 = 18
# NULL = __null # alias
CODEC_ID_MSMPEG4V3 = 17
CODEC_ID_MSMPEG4V2 = 16
CODEC_ID_MSMPEG4V1 = 15
# def DECLARE_ALIGNED(n,t,v): return t __attribute__ ((aligned (n))) v # macro
CODEC_ID_RAWVIDEO = 14
CODEC_ID_MPEG4 = 13
# __CLOCKID_T_TYPE = __S32_TYPE # alias
CODEC_ID_JPEGLS = 12
CODEC_ID_SP5X = 11
CODEC_ID_TEXT = 94210
CODEC_ID_LJPEG = 10
CODEC_ID_MJPEGB = 9
# def __LDBL_REDIR_NTH(name,proto): return name proto __THROW # macro
CODEC_ID_MJPEG = 8
SUBTITLE_BITMAP = 1
FP_SUBNORMAL = FP_SUBNORMAL # alias
CODEC_ID_RV20 = 7
CODEC_ID_RV10 = 6
CODEC_ID_H263 = 5
CODEC_ID_H261 = 4
CODEC_ID_MPEG2VIDEO_XVMC = 3
CODEC_ID_MPEG2VIDEO = 2
CODEC_ID_MPEG1VIDEO = 1
CODEC_ID_PCM_U24LE = 65550
CODEC_ID_NONE = 0
FF_LAMBDA_SCALE = 128 # Variable c_int '128'
FF_QUALITY_SCALE = FF_LAMBDA_SCALE # alias
_POSIX2_LINE_MAX = 2048 # Variable c_int '2048'
NL_LANGMAX = _POSIX2_LINE_MAX # alias
def AV_VERSION_INT(a,b,c): return (a<<16 | b<<8 | c) # macro
# def __LDBL_REDIR1_NTH(name,proto,alias): return name proto __THROW # macro
FP_NORMAL = 4
FP_NORMAL = FP_NORMAL # alias
CODEC_ID_CDXL = 161
CODEC_ID_PCM_S24BE = 65549
# LONG_MAX = __LONG_MAX__ # alias
_ISOC_ = 3
def __bswap_constant_32(x): return ((((x) & 0xff000000) >> 24) | (((x) & 0x00ff0000) >> 8) | (((x) & 0x0000ff00) << 8) | (((x) & 0x000000ff) << 24)) # macro
AVSTREAM_PARSE_TIMESTAMPS = 3
PIX_FMT_RGB565BE = 43
# def __MATHDECLX(type,function,suffix,args,attrib): return __MATHDECL_1(type, function,suffix, args) __attribute__ (attrib); __MATHDECL_1(type, __CONCAT(__,function),suffix, args) __attribute__ (attrib) # macro
_POSIX_ARG_MAX = 4096 # Variable c_int '4096'
NL_ARGMAX = _POSIX_ARG_MAX # alias
CODEC_ID_SONIC = 1397706307
_IO_ssize_t = _G_ssize_t # alias
CODEC_ID_PCM_S24LE = 65548
CODEC_ID_UTVIDEO = 155
_POSIX_ = 2
def __GNUC_PREREQ(maj,min): return ((__GNUC__ << 16) + __GNUC_MINOR__ >= ((maj) << 16) + (min)) # macro
CODEC_ID_8SVX_RAW = 944985688
CODEC_ID_PCM_U32BE = 65547
_XOPEN_ = 1
# def __FD_SET(d,set): return ((void) (__FDS_BITS (set)[__FDELT (d)] |= __FDMASK (d))) # macro
AV_ROUND_DOWN = 2
LIBAVFILTER_VERSION_INT = 152164 # Variable c_int '152164'
LIBAVFILTER_BUILD = LIBAVFILTER_VERSION_INT # alias
def __FD_ISSET(d,set): return ((__FDS_BITS (set)[__FDELT (d)] & __FDMASK (d)) != 0) # macro
class _G_fpos_t(Structure):
    pass
class __mbstate_t(Structure):
    pass
class N11__mbstate_t3DOT_7E(Union):
    pass
N11__mbstate_t3DOT_7E._fields_ = [
    ('__wch', c_uint),
    ('__wchb', c_char * 4),
]
__mbstate_t._fields_ = [
    ('__count', c_int),
    ('__value', N11__mbstate_t3DOT_7E),
]
_G_fpos_t._fields_ = [
    ('__pos', __off_t),
    ('__state', __mbstate_t),
]
_IO_pos_t = _G_fpos_t # alias
# def __FDMASK(d): return ((__fd_mask) 1 << ((d) % __NFDBITS)) # macro
PIX_FMT_RGB48LE = 42
def __FDELT(d): return ((d) / __NFDBITS) # macro
def isxdigit_l(c,l): return __isxdigit_l ((c), (l)) # macro
def __GLIBC_PREREQ(maj,min): return ((__GLIBC__ << 16) + __GLIBC_MINOR__ >= ((maj) << 16) + (min)) # macro
CODEC_ID_ILBC = 86076
CODEC_ID_KGV1 = 140
def __toascii(c): return ((c) & 0x7f) # macro
_IEEE_ = -1
CODEC_ID_IFF_BYTERUN1 = 139
AVCHROMA_LOC_NB = 7
AV_LOCK_DESTROY = 3
PIX_FMT_RGB48BE = 41
CODEC_ID_INDEO5 = 114
AVCOL_SPC_RGB = 0
AV_LOCK_OBTAIN = 1
CODEC_ID_IAC = 86075
__codecvt_partial = 1
def isascii_l(c,l): return __isascii_l ((c), (l)) # macro
stderr = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'stderr')
stderr = stderr # alias
__FD_SETSIZE = 1024 # Variable c_int '1024'
FD_SETSIZE = __FD_SETSIZE # alias
# def __bswap_constant_16(x): return ((unsigned short int) ((((x) >> 8) & 0xff) | (((x) & 0xff) << 8))) # macro
PIX_FMT_VDPAU_VC1 = 40
_POSIX2_EXPR_NEST_MAX = 32 # Variable c_int '32'
EXPR_NEST_MAX = _POSIX2_EXPR_NEST_MAX # alias
# def AV_PRAGMA(s): return _Pragma(#s) # macro
def isprint_l(c,l): return __isprint_l ((c), (l)) # macro
# def _IO_ferror_unlocked(__fp): return (((__fp)->_flags & _IO_ERR_SEEN) != 0) # macro
CODEC_ID_RALF = 86074
def offsetof(TYPE,MEMBER): return __builtin_offsetof (TYPE, MEMBER) # macro
# def _IO_feof_unlocked(__fp): return (((__fp)->_flags & _IO_EOF_SEEN) != 0) # macro
CODEC_ID_V210 = 129
# def _IO_PENDING_OUTPUT_COUNT(_fp): return ((_fp)->_IO_write_ptr - (_fp)->_IO_write_base) # macro
PIX_FMT_VDPAU_WMV3 = 39
CODEC_ID_TMV = 128
AVLINK_UNINIT = 0
CODEC_ID_SUNRAST = 112
def _IO_BE(expr,res): return __builtin_expect ((expr), res) # macro
CODEC_ID_AURA2 = 126
def _G_FSTAT64(fd,buf): return __fxstat64 (_STAT_VER, fd, buf) # macro
CODEC_ID_BMV_AUDIO = 86073
def minor(dev): return gnu_dev_minor (dev) # macro
# _IO_iconv_t = _G_iconv_t # alias
CODEC_ID_AURA = 125
AV_PICTURE_TYPE_SI = 5
def WTERMSIG(status): return __WTERMSIG (__WAIT_INT (status)) # macro
PIX_FMT_VDPAU_MPEG2 = 38
def WSTOPSIG(status): return __WSTOPSIG (__WAIT_INT (status)) # macro
# def FFSWAP(type,a,b): return do{type SWAP_tmp= b; b= a; a= SWAP_tmp;}while(0) # macro
CODEC_ID_TGV = 122
def WIFSIGNALED(status): return __WIFSIGNALED (__WAIT_INT (status)) # macro
CODEC_ID_8SVX_FIB = 86072
CODEC_ID_BFI = 119
def WEXITSTATUS(status): return __WEXITSTATUS (__WAIT_INT (status)) # macro
CODEC_ID_VB = 110
def AV_NE(be,le): return (le) # macro
CODEC_ID_DIRAC = 118
def AV_STRINGIFY(s): return AV_TOSTRING(s) # macro
EDEADLK = 35 # Variable c_int '35'
EDEADLOCK = EDEADLK # alias
_ISpunct = 4
CODEC_ID_RL2 = 116
AVCHROMA_LOC_BOTTOM = 6
def UINT64_C(c): return c ## UL # macro
CODEC_ID_MIMIC = 115
PIX_FMT_VDPAU_H264 = 36
_ISprint = 16384
CODEC_ID_FIRST_AUDIO = 65536
SCHAR_MIN = -128 # Variable c_int '-0x00000000000000080'
CHAR_MIN = SCHAR_MIN # alias
AVFMT_DURATION_FROM_BITRATE = 2
# def ROUNDED_DIV(a,b): return (((a)>0 ? (a) + ((b)>>1) : (a) - ((b)>>1))/(b)) # macro
def major(dev): return gnu_dev_major (dev) # macro
_ISdigit = 2048
_IO_off_t = _G_off_t # alias
PIX_FMT_YUVA420P = 35
CODEC_ID_AMV = 109
def putc(_ch,_fp): return _IO_putc (_ch, _fp) # macro
CODEC_ID_VP6A = 108
# SCHAR_MAX = __SCHAR_MAX__ # alias
# CHAR_MAX = SCHAR_MAX # alias
FP_ZERO = 2
_ISupper = 256
_G_HAVE_SYS_WAIT = 1 # Variable c_int '1'
_IO_HAVE_SYS_WAIT = _G_HAVE_SYS_WAIT # alias
def isalnum_l(c,l): return __isalnum_l ((c), (l)) # macro
AVCHROMA_LOC_UNSPECIFIED = 0
PIX_FMT_YUVJ440P = 34
CODEC_ID_C93 = 104
def INT64_C(c): return c ## L # macro
CODEC_ID_SGI = 103
# av_clip_uintp2 = av_clip_uintp2_c # alias
# __INO64_T_TYPE = __UQUAD_TYPE # alias
AV_MATRIX_ENCODING_NB = 3
def htobe64(x): return __bswap_64 (x) # macro
AV_MATRIX_ENCODING_DOLBY = 1
AVSTREAM_PARSE_NONE = 0
AV_MATRIX_ENCODING_NONE = 0
CODEC_ID_DXA = 100
AV_FIELD_BB = 3
AV_FIELD_TT = 2
AV_FIELD_PROGRESSIVE = 1
AV_FIELD_UNKNOWN = 0
AVCOL_PRI_NB = 9
AVCOL_PRI_FILM = 8
AVCOL_PRI_SMPTE170M = 6
AVCOL_PRI_BT470BG = 5
AVCOL_PRI_BT709 = 1
def getc(_fp): return _IO_getc (_fp) # macro
BYTE_ORDER = __BYTE_ORDER # alias
AVDISCARD_BIDIR = 16
_G_BUFSIZ = 8192 # Variable c_int '8192'
_IO_BUFSIZ = _G_BUFSIZ # alias
# av_clipf = av_clipf_c # alias
def FD_SET(fd,fdsetp): return __FD_SET (fd, fdsetp) # macro
AV_PICTURE_TYPE_BI = 7
AV_PICTURE_TYPE_SP = 6
CODEC_ID_VP6F = 94
AV_PICTURE_TYPE_B = 3
def FD_CLR(fd,fdsetp): return __FD_CLR (fd, fdsetp) # macro
def __isdigit_l(c,l): return __isctype_l((c), _ISdigit, (l)) # macro
# def av_dlog(pctx,...): return do { if (0) av_log(pctx, AV_LOG_DEBUG, __VA_ARGS__); } while (0) # macro
# def DECLARE_ASM_CONST(n,t,v): return static const t av_used __attribute__ ((aligned (n))) v # macro
def AVERROR(e): return (-(e)) # macro
ME_PHODS = 4
def alloca(size): return __builtin_alloca (size) # macro
__BIG_ENDIAN = 4321 # Variable c_int '4321'
BIG_ENDIAN = __BIG_ENDIAN # alias
AVDISCARD_DEFAULT = 0
CODEC_ID_MLP = 86045
# _G_wchar_t = wchar_t # alias
PIX_FMT_YUV422P9LE = 80
def AV_VERSION_DOT(a,b,c): return a ##. ## b ##. ## c # macro
CODEC_ID_VC1 = 72
CODEC_ID_SMACKVIDEO = 85
def AV_TOSTRING(s): return #s # macro
CODEC_ID_AVUI = 1096176969
AVDISCARD_NONE = -16
def __va_arg_pack_len(): return __builtin_va_arg_pack_len () # macro
CODEC_ID_CSCD = 81
CODEC_ID_TRUEMOTION2 = 79
def FFMAX3(a,b,c): return FFMAX(FFMAX(a,b),c) # macro
CODEC_ID_G2M = 4665933
def be16toh(x): return __bswap_16 (x) # macro
CODEC_ID_INDEO2 = 77
CODEC_ID_IMC = 86043
ME_ZERO = 1
def __WIFSTOPPED(status): return (((status) & 0xff) == 0x7f) # macro
# av_clip_int8 = av_clip_int8_c # alias
AVCOL_RANGE_UNSPECIFIED = 0
# def AV_GCC_VERSION_AT_LEAST(x,y): return (__GNUC__ > x || __GNUC__ == x && __GNUC_MINOR__ >= y) # macro
PIX_FMT_RGBA = 28
CODEC_ID_ESCAPE130 = 1160852272
CODEC_ID_MP4ALS = 86062
CODEC_ID_DSICINAUDIO = 86042
# av_clip_int16 = av_clip_int16_c # alias
AV_SAMPLE_FMT_NB = 10
AV_SAMPLE_FMT_DBLP = 9
# def _IO_peekc_unlocked(_fp): return (_IO_BE ((_fp)->_IO_read_ptr >= (_fp)->_IO_read_end, 0) && __underflow (_fp) == EOF ? EOF : *(unsigned char *) (_fp)->_IO_read_ptr) # macro
AV_SAMPLE_FMT_FLTP = 8
_POSIX2_BC_STRING_MAX = 1000 # Variable c_int '1000'
BC_STRING_MAX = _POSIX2_BC_STRING_MAX # alias
def __isascii_l(c,l): return ((l), __isascii (c)) # macro
# av_clip = av_clip_c # alias
AV_SAMPLE_FMT_S16P = 6
def INT16_C(c): return c # macro
EAGAIN = 11 # Variable c_int '11'
EWOULDBLOCK = EAGAIN # alias
# def GET_UTF8(val,GET_BYTE,ERROR): return val= GET_BYTE; { int ones= 7 - av_log2(val ^ 255); if(ones==1) ERROR val&= 127>>ones; while(--ones > 0){ int tmp= GET_BYTE - 128; if(tmp>>6) ERROR val= (val<<6) + tmp; } } # macro
CODEC_ID_PNG = 63
# def signbit(x): return (sizeof (x) == sizeof (float) ? __signbitf (x) : sizeof (x) == sizeof (double) ? __signbit (x) : __signbitl (x)) # macro
def FFUMOD(a,b): return ((a)-(b)*FFUDIV(a,b)) # macro
CODEC_ID_QPEG = 62
# def FFSIGN(a): return ((a) > 0 ? 1 : -1) # macro
def FFMIN3(a,b,c): return FFMIN(FFMIN(a,b),c) # macro
CODEC_ID_VIXL = 61
PIX_FMT_YUV422P9BE = 79
# def FFMAX(a,b): return ((a) > (b) ? (a) : (b)) # macro
AV_SAMPLE_FMT_S16 = 1
def FF_ARRAY_ELEMS(a): return (sizeof(a) / sizeof((a)[0])) # macro
CODEC_ID_Y41P = 1496592720
AV_SAMPLE_FMT_NONE = -1
# def FFUDIV(a,b): return (((a)>0 ?(a):(a)-(b)+1) / (b)) # macro
CODEC_ID_SMACKAUDIO = 86039
CODEC_ID_ADPCM_IMA_WS = 69636
# av_builtin_constant_p = __builtin_constant_p # alias
AV_CLASS_CATEGORY_NB = 9
AV_CLASS_CATEGORY_BITSTREAM_FILTER = 8
AV_CLASS_CATEGORY_FILTER = 7
AV_CLASS_CATEGORY_DECODER = 6
AV_CLASS_CATEGORY_ENCODER = 5
AV_CLASS_CATEGORY_DEMUXER = 4
AV_CLASS_CATEGORY_MUXER = 3
AV_CLASS_CATEGORY_INPUT = 1
AV_CLASS_CATEGORY_NA = 0
# def FFMIN(a,b): return ((a) > (b) ? (b) : (a)) # macro
# def _IO_getc_unlocked(_fp): return (_IO_BE ((_fp)->_IO_read_ptr >= (_fp)->_IO_read_end, 0) ? __uflow (_fp) : *(unsigned char *) (_fp)->_IO_read_ptr++) # macro
# def __WIFSIGNALED(status): return (((signed char) (((status) & 0x7f) + 1) >> 1) > 0) # macro
CODEC_ID_SMC = 50
SUBTITLE_NONE = 0
CODEC_ID_MPEG2TS = 131072
FP_NAN = 0
_POSIX2_BC_DIM_MAX = 2048 # Variable c_int '2048'
BC_DIM_MAX = _POSIX2_BC_DIM_MAX # alias
def __isalpha_l(c,l): return __isctype_l((c), _ISalpha, (l)) # macro
CODEC_ID_ADPCM_EA_MAXIS_XA = 69658
CODEC_ID_ADPCM_EA_XAS = 69657
CODEC_ID_ADPCM_IMA_EA_EACS = 69656
CODEC_ID_ADPCM_EA_R2 = 69654
CODEC_ID_ADPCM_EA_R1 = 69652
PIX_FMT_RGB8 = 22
CODEC_ID_ADPCM_IMA_AMV = 69651
CODEC_ID_ADPCM_THP = 69650
CODEC_ID_ADPCM_SBPRO_2 = 69649
CODEC_ID_ADPCM_SBPRO_3 = 69648
PIX_FMT_NB = 301
PIX_FMT_YUVA422P = 300
PIX_FMT_YUVA444P = 299
CODEC_ID_ADPCM_G726 = 69643
# def AV_NOWARN_DEPRECATED(code): return _Pragma("GCC diagnostic push") _Pragma("GCC diagnostic ignored \"-Wdeprecated-declarations\"") code _Pragma("GCC diagnostic pop") # macro
PIX_FMT_0BGR = 297
PIX_FMT_RGB0 = 296
PIX_FMT_0RGB = 295
CODEC_ID_ADPCM_4XM = 69639
CODEC_ID_ADPCM_MS = 69638
CODEC_ID_ADPCM_IMA_SMJPEG = 69637
CODEC_ID_ATRAC3P = 86056
PIX_FMT_RGBA64BE = 291
CODEC_ID_ADPCM_IMA_DK4 = 69635
__off64_t = c_long
_G_off64_t = __off64_t # alias
CODEC_ID_ADPCM_IMA_DK3 = 69634
CODEC_ID_XAN_WC4 = 42
CODEC_ID_ADPCM_IMA_WAV = 69633
stdin = (POINTER(_IO_FILE)).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'stdin')
stdin = stdin # alias
PIX_FMT_GBRP9LE = 84
CODEC_ID_S302M = 65562
def __isalnum_l(c,l): return __isctype_l((c), _ISalnum, (l)) # macro
PIX_FMT_GBRP = 82
CODEC_ID_PCM_BLURAY = 65560
CODEC_ID_PCM_F64LE = 65559
CODEC_ID_PCM_F64BE = 65558
CODEC_ID_PCM_F32LE = 65557
PIX_FMT_YUV444P10BE = 77
CODEC_ID_PCM_DVD = 65555
CODEC_ID_PCM_ZORK = 65553
CODEC_ID_PCM_S24DAUD = 65552
CODEC_ID_PCM_U24BE = 65551
PIX_FMT_YUV420P10BE = 71
PIX_FMT_YUV420P9LE = 70
PIX_FMT_YUV420P9BE = 69
CODEC_ID_ROQ = 39
PIX_FMT_BGR48LE = 68
PIX_FMT_BGR48BE = 67
CODEC_ID_PCM_S32BE = 65545
# __wur = __attribute_warn_unused_result__ # alias
# __gwchar_t = wchar_t # alias
# __WCHAR_MAX = __WCHAR_MAX__ # alias
# __USECONDS_T_TYPE = __U32_TYPE # alias
# __UID_T_TYPE = __U32_TYPE # alias
# __TIME_T_TYPE = __SLONGWORD_TYPE # alias
# __SWBLK_T_TYPE = __SLONGWORD_TYPE # alias
# __SUSECONDS_T_TYPE = __SLONGWORD_TYPE # alias
# __SSIZE_T_TYPE = __SWORD_TYPE # alias
PIX_FMT_YUV444P10LE = 78
# __SLONG32_TYPE = int # alias
CODEC_ID_RV30 = 70
PIX_FMT_YUV420P16BE = 55
AVCOL_SPC_YCOCG = 8
AVCOL_SPC_YCGCO = AVCOL_SPC_YCOCG # alias
# __RLIM64_T_TYPE = __UQUAD_TYPE # alias
def __bos0(ptr): return __builtin_object_size (ptr, 0) # macro
# __OFF64_T_TYPE = __SQUAD_TYPE # alias
# __NLINK_T_TYPE = __UWORD_TYPE # alias
# def av_err2str(errnum): return av_make_error_string((char[AV_ERROR_MAX_STRING_SIZE]){0}, AV_ERROR_MAX_STRING_SIZE, errnum) # macro
PIX_FMT_BGR565BE = 47
# __KEY_T_TYPE = __S32_TYPE # alias
CODEC_ID_4XM = 35
PIX_FMT_BGR4 = 20
# __INO_T_TYPE = __ULONGWORD_TYPE # alias
PIX_FMT_RGB565LE = 44
# __ID_T_TYPE = __U32_TYPE # alias
# __GID_T_TYPE = __U32_TYPE # alias
# __FSFILCNT64_T_TYPE = __UQUAD_TYPE # alias
CODEC_ID_FFV1 = 34
# __FSBLKCNT_T_TYPE = __ULONGWORD_TYPE # alias
# __FSBLKCNT64_T_TYPE = __UQUAD_TYPE # alias
__FLOAT_WORD_ORDER = __BYTE_ORDER # alias
# __CLOCK_T_TYPE = __SLONGWORD_TYPE # alias
PIX_FMT_GRAY16LE = 32
# __BLKCNT_T_TYPE = __SLONGWORD_TYPE # alias
# __BLKCNT64_T_TYPE = __SQUAD_TYPE # alias
CODEC_ID_ASV1 = 32
_POSIX_PIPE_BUF = 512 # Variable c_int '512'
_POSIX_HIWAT = _POSIX_PIPE_BUF # alias
_POSIX_OPEN_MAX = 20 # Variable c_int '20'
_POSIX_FD_SETSIZE = _POSIX_OPEN_MAX # alias
# _Mfloat_ = float # alias
PIX_FMT_RGB4_BYTE = 24
PIX_FMT_RGB4 = 23
__uid_t = c_uint
_G_uid_t = __uid_t # alias
_IO_uid_t = _G_uid_t # alias
PIX_FMT_BGR4_BYTE = 21
PIX_FMT_UYYVYY411 = 18
_IO_off64_t = _G_off64_t # alias
PIX_FMT_XVMC_MPEG2_MC = 15
_IO_fpos_t = _G_fpos_t # alias
PIX_FMT_YUVJ422P = 13
PIX_FMT_YUVJ420P = 12
AVSTREAM_PARSE_FULL = 1
PIX_FMT_PAL8 = 11
PIX_FMT_MONOBLACK = 10
CODEC_ID_INDEO3 = 29
PIX_FMT_GBRP10LE = 86
PIX_FMT_YUV411P = 7
PIX_FMT_YUV410P = 6
CODEC_ID_V410 = 159
PIX_FMT_YUV422P = 4
PIX_FMT_BGR24 = 3
AV_SAMPLE_FMT_U8P = 5
PIX_FMT_RGB24 = 2
PIX_FMT_YUYV422 = 1
AVCOL_RANGE_JPEG = 2
PIX_FMT_YUV420P = 0
PIX_FMT_NONE = -1
# _G_VTABLE_LABEL_PREFIX_ID = __vt_ # alias
# _G_MMAP64 = __mmap64 # alias
# def __exctype(name): return extern int name (int) __THROW # macro
# _G_LSEEK64 = __lseek64 # alias
# SSIZE_MAX = LONG_MAX # alias
# SHRT_MAX = __SHRT_MAX__ # alias
int8_t = c_int8
QP_STORE_T = int8_t # alias
PIX_FMT_GBR24P = PIX_FMT_GBRP # alias
# NL_SETMAX = INT_MAX # alias
PIX_FMT_GBRP10BE = 85
# LLONG_MAX = __LONG_LONG_MAX__ # alias
LINE_MAX = _POSIX2_LINE_MAX # alias
LIBSWSCALE_VERSION_INT = 131428 # Variable c_int '131428'
LIBSWSCALE_BUILD = LIBSWSCALE_VERSION_INT # alias
LIBPOSTPROC_VERSION_INT = 3407972 # Variable c_int '3407972'
LIBPOSTPROC_BUILD = LIBPOSTPROC_VERSION_INT # alias
LIBAVUTIL_VERSION_INT = 3357796 # Variable c_int '3357796'
LIBAVUTIL_BUILD = LIBAVUTIL_VERSION_INT # alias
LIBAVFORMAT_VERSION_INT = 3541860 # Variable c_int '3541860'
LIBAVFORMAT_BUILD = LIBAVFORMAT_VERSION_INT # alias
LIBAVDEVICE_VERSION_INT = 3539044 # Variable c_int '3539044'
LIBAVDEVICE_BUILD = LIBAVDEVICE_VERSION_INT # alias
LIBAVCODEC_VERSION_INT = 3546468 # Variable c_int '3546468'
LIBAVCODEC_BUILD = LIBAVCODEC_VERSION_INT # alias
FP_ZERO = FP_ZERO # alias
FP_NAN = FP_NAN # alias
PIX_FMT_VAAPI_MOCO = 51
EOPNOTSUPP = 95 # Variable c_int '95'
ENOTSUP = EOPNOTSUPP # alias
def _G_ARGS(ARGLIST): return ARGLIST # macro
# CHAR_BIT = __CHAR_BIT__ # alias
BUFSIZ = _IO_BUFSIZ # alias
CODEC_ID_MP3ADU = 86029
# def __bswap_constant_64(x): return ((((x) & 0xff00000000000000ull) >> 56) | (((x) & 0x00ff000000000000ull) >> 40) | (((x) & 0x0000ff0000000000ull) >> 24) | (((x) & 0x000000ff00000000ull) >> 8) | (((x) & 0x00000000ff000000ull) << 8) | (((x) & 0x0000000000ff0000ull) << 24) | (((x) & 0x000000000000ff00ull) << 40) | (((x) & 0x00000000000000ffull) << 56)) # macro
AVFMT_DURATION_FROM_STREAM = 1
PIX_FMT_XVMC_MPEG2_IDCT = 16
AVCOL_SPC_NB = 9
AVFMT_DURATION_FROM_PTS = 0
AVCOL_SPC_SMPTE240M = 7
PIX_FMT_GBRP9BE = 83
AVCOL_SPC_UNSPECIFIED = 2
# def __FDS_BITS(set): return ((set)->fds_bits) # macro
AVFILTER_PACKED = 0
CODEC_ID_MP3ON4 = 86030
class _G_fpos64_t(Structure):
    pass
_G_fpos64_t._fields_ = [
    ('__pos', __off64_t),
    ('__state', __mbstate_t),
]
_IO_fpos64_t = _G_fpos64_t # alias
AV_CLASS_CATEGORY_OUTPUT = 2
AV_PICTURE_TYPE_NONE = 0
# def strdupa(s): return (__extension__ ({ __const char *__old = (s); size_t __len = strlen (__old) + 1; char *__new = (char *) __builtin_alloca (__len); (char *) memcpy (__new, __old, __len); })) # macro
# av_log2_16bit = av_log2_16bit_c # alias
PIX_FMT_VDA_VLD = 81
AV_AUDIO_SERVICE_TYPE_NB = 9
AV_AUDIO_SERVICE_TYPE_KARAOKE = 8
AV_AUDIO_SERVICE_TYPE_VOICE_OVER = 7
AV_AUDIO_SERVICE_TYPE_COMMENTARY = 5
AV_AUDIO_SERVICE_TYPE_DIALOGUE = 4
AV_AUDIO_SERVICE_TYPE_HEARING_IMPAIRED = 3
AV_AUDIO_SERVICE_TYPE_VISUALLY_IMPAIRED = 2
AV_AUDIO_SERVICE_TYPE_EFFECTS = 1
AV_AUDIO_SERVICE_TYPE_MAIN = 0
# def __bswap_64(x): return (__extension__ ({ register unsigned long __v, __x = (x); if (__builtin_constant_p (__x)) __v = __bswap_constant_64 (__x); else __asm__ ("bswap %q0" : "=r" (__v) : "0" (__x)); __v; })) # macro
CODEC_ID_ADPCM_EA_R3 = 69653
AV_SAMPLE_FMT_U8 = 0

# values for enumeration 'CodecID'
CodecID = c_int # enum

# values for enumeration 'Motion_Est_ID'
Motion_Est_ID = c_int # enum

# values for enumeration 'AVDiscard'
AVDiscard = c_int # enum

# values for enumeration 'AVColorPrimaries'
AVColorPrimaries = c_int # enum

# values for enumeration 'AVColorTransferCharacteristic'
AVColorTransferCharacteristic = c_int # enum

# values for enumeration 'AVColorSpace'
AVColorSpace = c_int # enum

# values for enumeration 'AVColorRange'
AVColorRange = c_int # enum

# values for enumeration 'AVChromaLocation'
AVChromaLocation = c_int # enum

# values for enumeration 'AVAudioServiceType'
AVAudioServiceType = c_int # enum
class RcOverride(Structure):
    pass
RcOverride._fields_ = [
    ('start_frame', c_int),
    ('end_frame', c_int),
    ('qscale', c_int),
    ('quality_factor', c_float),
]
class AVPanScan(Structure):
    pass
int16_t = c_int16
AVPanScan._fields_ = [
    ('id', c_int),
    ('width', c_int),
    ('height', c_int),
    ('position', int16_t * 2 * 3),
]

# values for enumeration 'AVPacketSideDataType'
AVPacketSideDataType = c_int # enum
class AVPacket(Structure):
    pass
int64_t = c_int64
uint8_t = c_uint8
class N8AVPacket4DOT_31E(Structure):
    pass
AVPacket._fields_ = [
    ('pts', int64_t),
    ('dts', int64_t),
    ('data', POINTER(uint8_t)),
    ('size', c_int),
    ('stream_index', c_int),
    ('flags', c_int),
    ('side_data', POINTER(N8AVPacket4DOT_31E)),
    ('side_data_elems', c_int),
    ('duration', c_int),
    ('destruct', CFUNCTYPE(None, POINTER(AVPacket))),
    ('priv', c_void_p),
    ('pos', int64_t),
    ('convergence_duration', int64_t),
]
N8AVPacket4DOT_31E._fields_ = [
    ('data', POINTER(uint8_t)),
    ('size', c_int),
    ('type', AVPacketSideDataType),
]

# values for enumeration 'AVSideDataParamChangeFlags'
AVSideDataParamChangeFlags = c_int # enum
class AVFrame(Structure):
    pass

# values for enumeration 'AVPictureType'
AVPictureType = c_int # enum
class AVRational(Structure):
    pass
AVRational._fields_ = [
    ('num', c_int),
    ('den', c_int),
]
uint32_t = c_uint32
uint64_t = c_uint64
class AVCodecContext(Structure):
    pass
AVFrame._fields_ = [
    ('data', POINTER(uint8_t) * 8),
    ('linesize', c_int * 8),
    ('extended_data', POINTER(POINTER(uint8_t))),
    ('width', c_int),
    ('height', c_int),
    ('nb_samples', c_int),
    ('format', c_int),
    ('key_frame', c_int),
    ('pict_type', AVPictureType),
    ('base', POINTER(uint8_t) * 8),
    ('sample_aspect_ratio', AVRational),
    ('pts', int64_t),
    ('pkt_pts', int64_t),
    ('pkt_dts', int64_t),
    ('coded_picture_number', c_int),
    ('display_picture_number', c_int),
    ('quality', c_int),
    ('reference', c_int),
    ('qscale_table', POINTER(int8_t)),
    ('qstride', c_int),
    ('qscale_type', c_int),
    ('mbskip_table', POINTER(uint8_t)),
    ('motion_val', POINTER(int16_t * 2) * 2),
    ('mb_type', POINTER(uint32_t)),
    ('dct_coeff', POINTER(c_short)),
    ('ref_index', POINTER(int8_t) * 2),
    ('opaque', c_void_p),
    ('error', uint64_t * 8),
    ('type', c_int),
    ('repeat_pict', c_int),
    ('interlaced_frame', c_int),
    ('top_field_first', c_int),
    ('palette_has_changed', c_int),
    ('buffer_hints', c_int),
    ('pan_scan', POINTER(AVPanScan)),
    ('reordered_opaque', int64_t),
    ('hwaccel_picture_private', c_void_p),
    ('owner', POINTER(AVCodecContext)),
    ('thread_opaque', c_void_p),
    ('motion_subsample_log2', uint8_t),
    ('sample_rate', c_int),
    ('channel_layout', uint64_t),
    ('best_effort_timestamp', int64_t),
    ('pkt_pos', int64_t),
    ('pkt_duration', int64_t),
]
av_frame_get_best_effort_timestamp = _libraries['/usr/local/lib/libavcodec.so'].av_frame_get_best_effort_timestamp
av_frame_get_best_effort_timestamp.restype = int64_t
av_frame_get_best_effort_timestamp.argtypes = [POINTER(AVFrame)]
av_frame_get_pkt_duration = _libraries['/usr/local/lib/libavcodec.so'].av_frame_get_pkt_duration
av_frame_get_pkt_duration.restype = int64_t
av_frame_get_pkt_duration.argtypes = [POINTER(AVFrame)]
av_frame_get_pkt_pos = _libraries['/usr/local/lib/libavcodec.so'].av_frame_get_pkt_pos
av_frame_get_pkt_pos.restype = int64_t
av_frame_get_pkt_pos.argtypes = [POINTER(AVFrame)]
av_frame_get_channel_layout = _libraries['/usr/local/lib/libavcodec.so'].av_frame_get_channel_layout
av_frame_get_channel_layout.restype = int64_t
av_frame_get_channel_layout.argtypes = [POINTER(AVFrame)]
av_frame_get_sample_rate = _libraries['/usr/local/lib/libavcodec.so'].av_frame_get_sample_rate
av_frame_get_sample_rate.restype = c_int
av_frame_get_sample_rate.argtypes = [POINTER(AVFrame)]
av_frame_set_best_effort_timestamp = _libraries['/usr/local/lib/libavcodec.so'].av_frame_set_best_effort_timestamp
av_frame_set_best_effort_timestamp.restype = None
av_frame_set_best_effort_timestamp.argtypes = [POINTER(AVFrame), int64_t]
av_frame_set_pkt_duration = _libraries['/usr/local/lib/libavcodec.so'].av_frame_set_pkt_duration
av_frame_set_pkt_duration.restype = None
av_frame_set_pkt_duration.argtypes = [POINTER(AVFrame), int64_t]
av_frame_set_pkt_pos = _libraries['/usr/local/lib/libavcodec.so'].av_frame_set_pkt_pos
av_frame_set_pkt_pos.restype = None
av_frame_set_pkt_pos.argtypes = [POINTER(AVFrame), int64_t]
av_frame_set_channel_layout = _libraries['/usr/local/lib/libavcodec.so'].av_frame_set_channel_layout
av_frame_set_channel_layout.restype = None
av_frame_set_channel_layout.argtypes = [POINTER(AVFrame), int64_t]
av_frame_set_sample_rate = _libraries['/usr/local/lib/libavcodec.so'].av_frame_set_sample_rate
av_frame_set_sample_rate.restype = None
av_frame_set_sample_rate.argtypes = [POINTER(AVFrame), c_int]
class AVCodecInternal(Structure):
    pass
AVCodecInternal._fields_ = [
]

# values for enumeration 'AVFieldOrder'
AVFieldOrder = c_int # enum
class AVClass(Structure):
    pass

# values for enumeration 'AVMediaType'
AVMediaType = c_int # enum
class AVCodec(Structure):
    pass

# values for enumeration 'PixelFormat'
PixelFormat = c_int # enum
uint16_t = c_uint16

# values for enumeration 'AVSampleFormat'
AVSampleFormat = c_int # enum
class AVHWAccel(Structure):
    pass
AVCodecContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('log_level_offset', c_int),
    ('codec_type', AVMediaType),
    ('codec', POINTER(AVCodec)),
    ('codec_name', c_char * 32),
    ('codec_id', CodecID),
    ('codec_tag', c_uint),
    ('stream_codec_tag', c_uint),
    ('sub_id', c_int),
    ('priv_data', c_void_p),
    ('internal', POINTER(AVCodecInternal)),
    ('opaque', c_void_p),
    ('bit_rate', c_int),
    ('bit_rate_tolerance', c_int),
    ('global_quality', c_int),
    ('compression_level', c_int),
    ('flags', c_int),
    ('flags2', c_int),
    ('extradata', POINTER(uint8_t)),
    ('extradata_size', c_int),
    ('time_base', AVRational),
    ('ticks_per_frame', c_int),
    ('delay', c_int),
    ('width', c_int),
    ('height', c_int),
    ('coded_width', c_int),
    ('coded_height', c_int),
    ('gop_size', c_int),
    ('pix_fmt', PixelFormat),
    ('me_method', c_int),
    ('draw_horiz_band', CFUNCTYPE(None, POINTER(AVCodecContext), POINTER(AVFrame), POINTER(c_int), c_int, c_int, c_int)),
    ('get_format', CFUNCTYPE(PixelFormat, POINTER(AVCodecContext), POINTER(PixelFormat))),
    ('max_b_frames', c_int),
    ('b_quant_factor', c_float),
    ('rc_strategy', c_int),
    ('b_frame_strategy', c_int),
    ('luma_elim_threshold', c_int),
    ('chroma_elim_threshold', c_int),
    ('b_quant_offset', c_float),
    ('has_b_frames', c_int),
    ('mpeg_quant', c_int),
    ('i_quant_factor', c_float),
    ('i_quant_offset', c_float),
    ('lumi_masking', c_float),
    ('temporal_cplx_masking', c_float),
    ('spatial_cplx_masking', c_float),
    ('p_masking', c_float),
    ('dark_masking', c_float),
    ('slice_count', c_int),
    ('prediction_method', c_int),
    ('slice_offset', POINTER(c_int)),
    ('sample_aspect_ratio', AVRational),
    ('me_cmp', c_int),
    ('me_sub_cmp', c_int),
    ('mb_cmp', c_int),
    ('ildct_cmp', c_int),
    ('dia_size', c_int),
    ('last_predictor_count', c_int),
    ('pre_me', c_int),
    ('me_pre_cmp', c_int),
    ('pre_dia_size', c_int),
    ('me_subpel_quality', c_int),
    ('dtg_active_format', c_int),
    ('me_range', c_int),
    ('intra_quant_bias', c_int),
    ('inter_quant_bias', c_int),
    ('color_table_id', c_int),
    ('slice_flags', c_int),
    ('xvmc_acceleration', c_int),
    ('mb_decision', c_int),
    ('intra_matrix', POINTER(uint16_t)),
    ('inter_matrix', POINTER(uint16_t)),
    ('scenechange_threshold', c_int),
    ('noise_reduction', c_int),
    ('inter_threshold', c_int),
    ('quantizer_noise_shaping', c_int),
    ('me_threshold', c_int),
    ('mb_threshold', c_int),
    ('intra_dc_precision', c_int),
    ('skip_top', c_int),
    ('skip_bottom', c_int),
    ('border_masking', c_float),
    ('mb_lmin', c_int),
    ('mb_lmax', c_int),
    ('me_penalty_compensation', c_int),
    ('bidir_refine', c_int),
    ('brd_scale', c_int),
    ('keyint_min', c_int),
    ('refs', c_int),
    ('chromaoffset', c_int),
    ('scenechange_factor', c_int),
    ('mv0_threshold', c_int),
    ('b_sensitivity', c_int),
    ('color_primaries', AVColorPrimaries),
    ('color_trc', AVColorTransferCharacteristic),
    ('colorspace', AVColorSpace),
    ('color_range', AVColorRange),
    ('chroma_sample_location', AVChromaLocation),
    ('slices', c_int),
    ('field_order', AVFieldOrder),
    ('sample_rate', c_int),
    ('channels', c_int),
    ('sample_fmt', AVSampleFormat),
    ('frame_size', c_int),
    ('frame_number', c_int),
    ('block_align', c_int),
    ('cutoff', c_int),
    ('request_channels', c_int),
    ('channel_layout', uint64_t),
    ('request_channel_layout', uint64_t),
    ('audio_service_type', AVAudioServiceType),
    ('request_sample_fmt', AVSampleFormat),
    ('get_buffer', CFUNCTYPE(c_int, POINTER(AVCodecContext), POINTER(AVFrame))),
    ('release_buffer', CFUNCTYPE(None, POINTER(AVCodecContext), POINTER(AVFrame))),
    ('reget_buffer', CFUNCTYPE(c_int, POINTER(AVCodecContext), POINTER(AVFrame))),
    ('qcompress', c_float),
    ('qblur', c_float),
    ('qmin', c_int),
    ('qmax', c_int),
    ('max_qdiff', c_int),
    ('rc_qsquish', c_float),
    ('rc_qmod_amp', c_float),
    ('rc_qmod_freq', c_int),
    ('rc_buffer_size', c_int),
    ('rc_override_count', c_int),
    ('rc_override', POINTER(RcOverride)),
    ('rc_eq', STRING),
    ('rc_max_rate', c_int),
    ('rc_min_rate', c_int),
    ('rc_buffer_aggressivity', c_float),
    ('rc_initial_cplx', c_float),
    ('rc_max_available_vbv_use', c_float),
    ('rc_min_vbv_overflow_use', c_float),
    ('rc_initial_buffer_occupancy', c_int),
    ('coder_type', c_int),
    ('context_model', c_int),
    ('lmin', c_int),
    ('lmax', c_int),
    ('frame_skip_threshold', c_int),
    ('frame_skip_factor', c_int),
    ('frame_skip_exp', c_int),
    ('frame_skip_cmp', c_int),
    ('trellis', c_int),
    ('min_prediction_order', c_int),
    ('max_prediction_order', c_int),
    ('timecode_frame_start', int64_t),
    ('rtp_callback', CFUNCTYPE(None, POINTER(AVCodecContext), c_void_p, c_int, c_int)),
    ('rtp_payload_size', c_int),
    ('mv_bits', c_int),
    ('header_bits', c_int),
    ('i_tex_bits', c_int),
    ('p_tex_bits', c_int),
    ('i_count', c_int),
    ('p_count', c_int),
    ('skip_count', c_int),
    ('misc_bits', c_int),
    ('frame_bits', c_int),
    ('stats_out', STRING),
    ('stats_in', STRING),
    ('workaround_bugs', c_int),
    ('strict_std_compliance', c_int),
    ('error_concealment', c_int),
    ('debug', c_int),
    ('debug_mv', c_int),
    ('err_recognition', c_int),
    ('reordered_opaque', int64_t),
    ('hwaccel', POINTER(AVHWAccel)),
    ('hwaccel_context', c_void_p),
    ('error', uint64_t * 8),
    ('dct_algo', c_int),
    ('idct_algo', c_int),
    ('dsp_mask', c_uint),
    ('bits_per_coded_sample', c_int),
    ('bits_per_raw_sample', c_int),
    ('lowres', c_int),
    ('coded_frame', POINTER(AVFrame)),
    ('thread_count', c_int),
    ('thread_type', c_int),
    ('active_thread_type', c_int),
    ('thread_safe_callbacks', c_int),
    ('execute', CFUNCTYPE(c_int, POINTER(AVCodecContext), CFUNCTYPE(c_int, POINTER(AVCodecContext), c_void_p), c_void_p, POINTER(c_int), c_int, c_int)),
    ('execute2', CFUNCTYPE(c_int, POINTER(AVCodecContext), CFUNCTYPE(c_int, POINTER(AVCodecContext), c_void_p, c_int, c_int), c_void_p, POINTER(c_int), c_int)),
    ('thread_opaque', c_void_p),
    ('nsse_weight', c_int),
    ('profile', c_int),
    ('level', c_int),
    ('skip_loop_filter', AVDiscard),
    ('skip_idct', AVDiscard),
    ('skip_frame', AVDiscard),
    ('subtitle_header', POINTER(uint8_t)),
    ('subtitle_header_size', c_int),
    ('error_rate', c_int),
    ('pkt', POINTER(AVPacket)),
    ('vbv_delay', uint64_t),
    ('pts_correction_num_faulty_pts', int64_t),
    ('pts_correction_num_faulty_dts', int64_t),
    ('pts_correction_last_pts', int64_t),
    ('pts_correction_last_dts', int64_t),
]
class AVProfile(Structure):
    pass
AVProfile._fields_ = [
    ('profile', c_int),
    ('name', STRING),
]
class AVCodecDefault(Structure):
    pass
AVCodecDefault._fields_ = [
]
AVCodec._fields_ = [
    ('name', STRING),
    ('long_name', STRING),
    ('type', AVMediaType),
    ('id', CodecID),
    ('capabilities', c_int),
    ('supported_framerates', POINTER(AVRational)),
    ('pix_fmts', POINTER(PixelFormat)),
    ('supported_samplerates', POINTER(c_int)),
    ('sample_fmts', POINTER(AVSampleFormat)),
    ('channel_layouts', POINTER(uint64_t)),
    ('max_lowres', uint8_t),
    ('priv_class', POINTER(AVClass)),
    ('profiles', POINTER(AVProfile)),
    ('priv_data_size', c_int),
    ('next', POINTER(AVCodec)),
    ('init_thread_copy', CFUNCTYPE(c_int, POINTER(AVCodecContext))),
    ('update_thread_context', CFUNCTYPE(c_int, POINTER(AVCodecContext), POINTER(AVCodecContext))),
    ('defaults', POINTER(AVCodecDefault)),
    ('init_static_data', CFUNCTYPE(None, POINTER(AVCodec))),
    ('init', CFUNCTYPE(c_int, POINTER(AVCodecContext))),
    ('encode', CFUNCTYPE(c_int, POINTER(AVCodecContext), POINTER(uint8_t), c_int, c_void_p)),
    ('encode2', CFUNCTYPE(c_int, POINTER(AVCodecContext), POINTER(AVPacket), POINTER(AVFrame), POINTER(c_int))),
    ('decode', CFUNCTYPE(c_int, POINTER(AVCodecContext), c_void_p, POINTER(c_int), POINTER(AVPacket))),
    ('close', CFUNCTYPE(c_int, POINTER(AVCodecContext))),
    ('flush', CFUNCTYPE(None, POINTER(AVCodecContext))),
]
AVHWAccel._fields_ = [
    ('name', STRING),
    ('type', AVMediaType),
    ('id', CodecID),
    ('pix_fmt', PixelFormat),
    ('capabilities', c_int),
    ('next', POINTER(AVHWAccel)),
    ('start_frame', CFUNCTYPE(c_int, POINTER(AVCodecContext), POINTER(uint8_t), uint32_t)),
    ('decode_slice', CFUNCTYPE(c_int, POINTER(AVCodecContext), POINTER(uint8_t), uint32_t)),
    ('end_frame', CFUNCTYPE(c_int, POINTER(AVCodecContext))),
    ('priv_data_size', c_int),
]
class AVPicture(Structure):
    pass
AVPicture._fields_ = [
    ('data', POINTER(uint8_t) * 8),
    ('linesize', c_int * 8),
]

# values for enumeration 'AVSubtitleType'
AVSubtitleType = c_int # enum
class AVSubtitleRect(Structure):
    pass
AVSubtitleRect._fields_ = [
    ('x', c_int),
    ('y', c_int),
    ('w', c_int),
    ('h', c_int),
    ('nb_colors', c_int),
    ('pict', AVPicture),
    ('type', AVSubtitleType),
    ('text', STRING),
    ('ass', STRING),
    ('forced', c_int),
]
class AVSubtitle(Structure):
    pass
AVSubtitle._fields_ = [
    ('format', uint16_t),
    ('start_display_time', uint32_t),
    ('end_display_time', uint32_t),
    ('num_rects', c_uint),
    ('rects', POINTER(POINTER(AVSubtitleRect))),
    ('pts', int64_t),
]
av_codec_next = _libraries['/usr/local/lib/libavcodec.so'].av_codec_next
av_codec_next.restype = POINTER(AVCodec)
av_codec_next.argtypes = [POINTER(AVCodec)]
avcodec_version = _libraries['/usr/local/lib/libavcodec.so'].avcodec_version
avcodec_version.restype = c_uint
avcodec_version.argtypes = []
avcodec_configuration = _libraries['/usr/local/lib/libavcodec.so'].avcodec_configuration
avcodec_configuration.restype = STRING
avcodec_configuration.argtypes = []
avcodec_license = _libraries['/usr/local/lib/libavcodec.so'].avcodec_license
avcodec_license.restype = STRING
avcodec_license.argtypes = []
avcodec_register = _libraries['/usr/local/lib/libavcodec.so'].avcodec_register
avcodec_register.restype = None
avcodec_register.argtypes = [POINTER(AVCodec)]
avcodec_register_all = _libraries['/usr/local/lib/libavcodec.so'].avcodec_register_all
avcodec_register_all.restype = None
avcodec_register_all.argtypes = []
avcodec_alloc_context = _libraries['/usr/local/lib/libavcodec.so'].avcodec_alloc_context
avcodec_alloc_context.restype = POINTER(AVCodecContext)
avcodec_alloc_context.argtypes = []
avcodec_alloc_context2 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_alloc_context2
avcodec_alloc_context2.restype = POINTER(AVCodecContext)
avcodec_alloc_context2.argtypes = [AVMediaType]
avcodec_get_context_defaults = _libraries['/usr/local/lib/libavcodec.so'].avcodec_get_context_defaults
avcodec_get_context_defaults.restype = None
avcodec_get_context_defaults.argtypes = [POINTER(AVCodecContext)]
avcodec_get_context_defaults2 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_get_context_defaults2
avcodec_get_context_defaults2.restype = None
avcodec_get_context_defaults2.argtypes = [POINTER(AVCodecContext), AVMediaType]
avcodec_alloc_context3 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_alloc_context3
avcodec_alloc_context3.restype = POINTER(AVCodecContext)
avcodec_alloc_context3.argtypes = [POINTER(AVCodec)]
avcodec_get_context_defaults3 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_get_context_defaults3
avcodec_get_context_defaults3.restype = c_int
avcodec_get_context_defaults3.argtypes = [POINTER(AVCodecContext), POINTER(AVCodec)]
avcodec_get_class = _libraries['/usr/local/lib/libavcodec.so'].avcodec_get_class
avcodec_get_class.restype = POINTER(AVClass)
avcodec_get_class.argtypes = []
avcodec_get_frame_class = _libraries['/usr/local/lib/libavcodec.so'].avcodec_get_frame_class
avcodec_get_frame_class.restype = POINTER(AVClass)
avcodec_get_frame_class.argtypes = []
avcodec_get_subtitle_rect_class = _libraries['/usr/local/lib/libavcodec.so'].avcodec_get_subtitle_rect_class
avcodec_get_subtitle_rect_class.restype = POINTER(AVClass)
avcodec_get_subtitle_rect_class.argtypes = []
avcodec_copy_context = _libraries['/usr/local/lib/libavcodec.so'].avcodec_copy_context
avcodec_copy_context.restype = c_int
avcodec_copy_context.argtypes = [POINTER(AVCodecContext), POINTER(AVCodecContext)]
avcodec_alloc_frame = _libraries['/usr/local/lib/libavcodec.so'].avcodec_alloc_frame
avcodec_alloc_frame.restype = POINTER(AVFrame)
avcodec_alloc_frame.argtypes = []
avcodec_get_frame_defaults = _libraries['/usr/local/lib/libavcodec.so'].avcodec_get_frame_defaults
avcodec_get_frame_defaults.restype = None
avcodec_get_frame_defaults.argtypes = [POINTER(AVFrame)]
avcodec_open = _libraries['/usr/local/lib/libavcodec.so'].avcodec_open
avcodec_open.restype = c_int
avcodec_open.argtypes = [POINTER(AVCodecContext), POINTER(AVCodec)]
class AVDictionary(Structure):
    pass
avcodec_open2 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_open2
avcodec_open2.restype = c_int
avcodec_open2.argtypes = [POINTER(AVCodecContext), POINTER(AVCodec), POINTER(POINTER(AVDictionary))]
avcodec_close = _libraries['/usr/local/lib/libavcodec.so'].avcodec_close
avcodec_close.restype = c_int
avcodec_close.argtypes = [POINTER(AVCodecContext)]
avsubtitle_free = _libraries['/usr/local/lib/libavcodec.so'].avsubtitle_free
avsubtitle_free.restype = None
avsubtitle_free.argtypes = [POINTER(AVSubtitle)]
av_destruct_packet_nofree = _libraries['/usr/local/lib/libavcodec.so'].av_destruct_packet_nofree
av_destruct_packet_nofree.restype = None
av_destruct_packet_nofree.argtypes = [POINTER(AVPacket)]
av_destruct_packet = _libraries['/usr/local/lib/libavcodec.so'].av_destruct_packet
av_destruct_packet.restype = None
av_destruct_packet.argtypes = [POINTER(AVPacket)]
av_init_packet = _libraries['/usr/local/lib/libavcodec.so'].av_init_packet
av_init_packet.restype = None
av_init_packet.argtypes = [POINTER(AVPacket)]
av_new_packet = _libraries['/usr/local/lib/libavcodec.so'].av_new_packet
av_new_packet.restype = c_int
av_new_packet.argtypes = [POINTER(AVPacket), c_int]
av_shrink_packet = _libraries['/usr/local/lib/libavcodec.so'].av_shrink_packet
av_shrink_packet.restype = None
av_shrink_packet.argtypes = [POINTER(AVPacket), c_int]
av_grow_packet = _libraries['/usr/local/lib/libavcodec.so'].av_grow_packet
av_grow_packet.restype = c_int
av_grow_packet.argtypes = [POINTER(AVPacket), c_int]
av_dup_packet = _libraries['/usr/local/lib/libavcodec.so'].av_dup_packet
av_dup_packet.restype = c_int
av_dup_packet.argtypes = [POINTER(AVPacket)]
av_free_packet = _libraries['/usr/local/lib/libavcodec.so'].av_free_packet
av_free_packet.restype = None
av_free_packet.argtypes = [POINTER(AVPacket)]
av_packet_new_side_data = _libraries['/usr/local/lib/libavcodec.so'].av_packet_new_side_data
av_packet_new_side_data.restype = POINTER(uint8_t)
av_packet_new_side_data.argtypes = [POINTER(AVPacket), AVPacketSideDataType, c_int]
av_packet_shrink_side_data = _libraries['/usr/local/lib/libavcodec.so'].av_packet_shrink_side_data
av_packet_shrink_side_data.restype = c_int
av_packet_shrink_side_data.argtypes = [POINTER(AVPacket), AVPacketSideDataType, c_int]
av_packet_get_side_data = _libraries['/usr/local/lib/libavcodec.so'].av_packet_get_side_data
av_packet_get_side_data.restype = POINTER(uint8_t)
av_packet_get_side_data.argtypes = [POINTER(AVPacket), AVPacketSideDataType, POINTER(c_int)]
av_packet_merge_side_data = _libraries['/usr/local/lib/libavcodec.so'].av_packet_merge_side_data
av_packet_merge_side_data.restype = c_int
av_packet_merge_side_data.argtypes = [POINTER(AVPacket)]
av_packet_split_side_data = _libraries['/usr/local/lib/libavcodec.so'].av_packet_split_side_data
av_packet_split_side_data.restype = c_int
av_packet_split_side_data.argtypes = [POINTER(AVPacket)]
avcodec_find_decoder = _libraries['/usr/local/lib/libavcodec.so'].avcodec_find_decoder
avcodec_find_decoder.restype = POINTER(AVCodec)
avcodec_find_decoder.argtypes = [CodecID]
avcodec_find_decoder_by_name = _libraries['/usr/local/lib/libavcodec.so'].avcodec_find_decoder_by_name
avcodec_find_decoder_by_name.restype = POINTER(AVCodec)
avcodec_find_decoder_by_name.argtypes = [STRING]
avcodec_default_get_buffer = _libraries['/usr/local/lib/libavcodec.so'].avcodec_default_get_buffer
avcodec_default_get_buffer.restype = c_int
avcodec_default_get_buffer.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame)]
avcodec_default_release_buffer = _libraries['/usr/local/lib/libavcodec.so'].avcodec_default_release_buffer
avcodec_default_release_buffer.restype = None
avcodec_default_release_buffer.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame)]
avcodec_default_reget_buffer = _libraries['/usr/local/lib/libavcodec.so'].avcodec_default_reget_buffer
avcodec_default_reget_buffer.restype = c_int
avcodec_default_reget_buffer.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame)]
avcodec_get_edge_width = _libraries['/usr/local/lib/libavcodec.so'].avcodec_get_edge_width
avcodec_get_edge_width.restype = c_uint
avcodec_get_edge_width.argtypes = []
avcodec_align_dimensions = _libraries['/usr/local/lib/libavcodec.so'].avcodec_align_dimensions
avcodec_align_dimensions.restype = None
avcodec_align_dimensions.argtypes = [POINTER(AVCodecContext), POINTER(c_int), POINTER(c_int)]
avcodec_align_dimensions2 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_align_dimensions2
avcodec_align_dimensions2.restype = None
avcodec_align_dimensions2.argtypes = [POINTER(AVCodecContext), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
avcodec_decode_audio3 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_decode_audio3
avcodec_decode_audio3.restype = c_int
avcodec_decode_audio3.argtypes = [POINTER(AVCodecContext), POINTER(int16_t), POINTER(c_int), POINTER(AVPacket)]
avcodec_decode_audio4 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_decode_audio4
avcodec_decode_audio4.restype = c_int
avcodec_decode_audio4.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame), POINTER(c_int), POINTER(AVPacket)]
avcodec_decode_video2 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_decode_video2
avcodec_decode_video2.restype = c_int
avcodec_decode_video2.argtypes = [POINTER(AVCodecContext), POINTER(AVFrame), POINTER(c_int), POINTER(AVPacket)]
avcodec_decode_subtitle2 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_decode_subtitle2
avcodec_decode_subtitle2.restype = c_int
avcodec_decode_subtitle2.argtypes = [POINTER(AVCodecContext), POINTER(AVSubtitle), POINTER(c_int), POINTER(AVPacket)]
class AVCodecParserContext(Structure):
    pass
class AVCodecParser(Structure):
    pass
AVCodecParserContext._fields_ = [
    ('priv_data', c_void_p),
    ('parser', POINTER(AVCodecParser)),
    ('frame_offset', int64_t),
    ('cur_offset', int64_t),
    ('next_frame_offset', int64_t),
    ('pict_type', c_int),
    ('repeat_pict', c_int),
    ('pts', int64_t),
    ('dts', int64_t),
    ('last_pts', int64_t),
    ('last_dts', int64_t),
    ('fetch_timestamp', c_int),
    ('cur_frame_start_index', c_int),
    ('cur_frame_offset', int64_t * 4),
    ('cur_frame_pts', int64_t * 4),
    ('cur_frame_dts', int64_t * 4),
    ('flags', c_int),
    ('offset', int64_t),
    ('cur_frame_end', int64_t * 4),
    ('key_frame', c_int),
    ('convergence_duration', int64_t),
    ('dts_sync_point', c_int),
    ('dts_ref_dts_delta', c_int),
    ('pts_dts_delta', c_int),
    ('cur_frame_pos', int64_t * 4),
    ('pos', int64_t),
    ('last_pos', int64_t),
    ('duration', c_int),
]
AVCodecParser._fields_ = [
    ('codec_ids', c_int * 5),
    ('priv_data_size', c_int),
    ('parser_init', CFUNCTYPE(c_int, POINTER(AVCodecParserContext))),
    ('parser_parse', CFUNCTYPE(c_int, POINTER(AVCodecParserContext), POINTER(AVCodecContext), POINTER(POINTER(uint8_t)), POINTER(c_int), POINTER(uint8_t), c_int)),
    ('parser_close', CFUNCTYPE(None, POINTER(AVCodecParserContext))),
    ('split', CFUNCTYPE(c_int, POINTER(AVCodecContext), POINTER(uint8_t), c_int)),
    ('next', POINTER(AVCodecParser)),
]
av_parser_next = _libraries['/usr/local/lib/libavcodec.so'].av_parser_next
av_parser_next.restype = POINTER(AVCodecParser)
av_parser_next.argtypes = [POINTER(AVCodecParser)]
av_register_codec_parser = _libraries['/usr/local/lib/libavcodec.so'].av_register_codec_parser
av_register_codec_parser.restype = None
av_register_codec_parser.argtypes = [POINTER(AVCodecParser)]
av_parser_init = _libraries['/usr/local/lib/libavcodec.so'].av_parser_init
av_parser_init.restype = POINTER(AVCodecParserContext)
av_parser_init.argtypes = [c_int]
av_parser_parse2 = _libraries['/usr/local/lib/libavcodec.so'].av_parser_parse2
av_parser_parse2.restype = c_int
av_parser_parse2.argtypes = [POINTER(AVCodecParserContext), POINTER(AVCodecContext), POINTER(POINTER(uint8_t)), POINTER(c_int), POINTER(uint8_t), c_int, int64_t, int64_t, int64_t]
av_parser_change = _libraries['/usr/local/lib/libavcodec.so'].av_parser_change
av_parser_change.restype = c_int
av_parser_change.argtypes = [POINTER(AVCodecParserContext), POINTER(AVCodecContext), POINTER(POINTER(uint8_t)), POINTER(c_int), POINTER(uint8_t), c_int, c_int]
av_parser_close = _libraries['/usr/local/lib/libavcodec.so'].av_parser_close
av_parser_close.restype = None
av_parser_close.argtypes = [POINTER(AVCodecParserContext)]
avcodec_find_encoder = _libraries['/usr/local/lib/libavcodec.so'].avcodec_find_encoder
avcodec_find_encoder.restype = POINTER(AVCodec)
avcodec_find_encoder.argtypes = [CodecID]
avcodec_find_encoder_by_name = _libraries['/usr/local/lib/libavcodec.so'].avcodec_find_encoder_by_name
avcodec_find_encoder_by_name.restype = POINTER(AVCodec)
avcodec_find_encoder_by_name.argtypes = [STRING]
avcodec_encode_audio = _libraries['/usr/local/lib/libavcodec.so'].avcodec_encode_audio
avcodec_encode_audio.restype = c_int
avcodec_encode_audio.argtypes = [POINTER(AVCodecContext), POINTER(uint8_t), c_int, POINTER(c_short)]
avcodec_encode_audio2 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_encode_audio2
avcodec_encode_audio2.restype = c_int
avcodec_encode_audio2.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket), POINTER(AVFrame), POINTER(c_int)]
avcodec_encode_video = _libraries['/usr/local/lib/libavcodec.so'].avcodec_encode_video
avcodec_encode_video.restype = c_int
avcodec_encode_video.argtypes = [POINTER(AVCodecContext), POINTER(uint8_t), c_int, POINTER(AVFrame)]
avcodec_encode_video2 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_encode_video2
avcodec_encode_video2.restype = c_int
avcodec_encode_video2.argtypes = [POINTER(AVCodecContext), POINTER(AVPacket), POINTER(AVFrame), POINTER(c_int)]
avcodec_encode_subtitle = _libraries['/usr/local/lib/libavcodec.so'].avcodec_encode_subtitle
avcodec_encode_subtitle.restype = c_int
avcodec_encode_subtitle.argtypes = [POINTER(AVCodecContext), POINTER(uint8_t), c_int, POINTER(AVSubtitle)]
class ReSampleContext(Structure):
    pass
ReSampleContext._fields_ = [
]
class AVResampleContext(Structure):
    pass
AVResampleContext._fields_ = [
]
av_audio_resample_init = _libraries['/usr/local/lib/libavcodec.so'].av_audio_resample_init
av_audio_resample_init.restype = POINTER(ReSampleContext)
av_audio_resample_init.argtypes = [c_int, c_int, c_int, c_int, AVSampleFormat, AVSampleFormat, c_int, c_int, c_int, c_double]
audio_resample = _libraries['/usr/local/lib/libavcodec.so'].audio_resample
audio_resample.restype = c_int
audio_resample.argtypes = [POINTER(ReSampleContext), POINTER(c_short), POINTER(c_short), c_int]
audio_resample_close = _libraries['/usr/local/lib/libavcodec.so'].audio_resample_close
audio_resample_close.restype = None
audio_resample_close.argtypes = [POINTER(ReSampleContext)]
av_resample_init = _libraries['/usr/local/lib/libavcodec.so'].av_resample_init
av_resample_init.restype = POINTER(AVResampleContext)
av_resample_init.argtypes = [c_int, c_int, c_int, c_int, c_int, c_double]
av_resample = _libraries['/usr/local/lib/libavcodec.so'].av_resample
av_resample.restype = c_int
av_resample.argtypes = [POINTER(AVResampleContext), POINTER(c_short), POINTER(c_short), POINTER(c_int), c_int, c_int, c_int]
av_resample_compensate = _libraries['/usr/local/lib/libavcodec.so'].av_resample_compensate
av_resample_compensate.restype = None
av_resample_compensate.argtypes = [POINTER(AVResampleContext), c_int, c_int]
av_resample_close = _libraries['/usr/local/lib/libavcodec.so'].av_resample_close
av_resample_close.restype = None
av_resample_close.argtypes = [POINTER(AVResampleContext)]
avpicture_alloc = _libraries['/usr/local/lib/libavcodec.so'].avpicture_alloc
avpicture_alloc.restype = c_int
avpicture_alloc.argtypes = [POINTER(AVPicture), PixelFormat, c_int, c_int]
avpicture_free = _libraries['/usr/local/lib/libavcodec.so'].avpicture_free
avpicture_free.restype = None
avpicture_free.argtypes = [POINTER(AVPicture)]
avpicture_fill = _libraries['/usr/local/lib/libavcodec.so'].avpicture_fill
avpicture_fill.restype = c_int
avpicture_fill.argtypes = [POINTER(AVPicture), POINTER(uint8_t), PixelFormat, c_int, c_int]
avpicture_layout = _libraries['/usr/local/lib/libavcodec.so'].avpicture_layout
avpicture_layout.restype = c_int
avpicture_layout.argtypes = [POINTER(AVPicture), PixelFormat, c_int, c_int, POINTER(c_ubyte), c_int]
avpicture_get_size = _libraries['/usr/local/lib/libavcodec.so'].avpicture_get_size
avpicture_get_size.restype = c_int
avpicture_get_size.argtypes = [PixelFormat, c_int, c_int]
avpicture_deinterlace = _libraries['/usr/local/lib/libavcodec.so'].avpicture_deinterlace
avpicture_deinterlace.restype = c_int
avpicture_deinterlace.argtypes = [POINTER(AVPicture), POINTER(AVPicture), PixelFormat, c_int, c_int]
av_picture_copy = _libraries['/usr/local/lib/libavcodec.so'].av_picture_copy
av_picture_copy.restype = None
av_picture_copy.argtypes = [POINTER(AVPicture), POINTER(AVPicture), PixelFormat, c_int, c_int]
av_picture_crop = _libraries['/usr/local/lib/libavcodec.so'].av_picture_crop
av_picture_crop.restype = c_int
av_picture_crop.argtypes = [POINTER(AVPicture), POINTER(AVPicture), PixelFormat, c_int, c_int]
av_picture_pad = _libraries['/usr/local/lib/libavcodec.so'].av_picture_pad
av_picture_pad.restype = c_int
av_picture_pad.argtypes = [POINTER(AVPicture), POINTER(AVPicture), c_int, c_int, PixelFormat, c_int, c_int, c_int, c_int, POINTER(c_int)]
avcodec_get_chroma_sub_sample = _libraries['/usr/local/lib/libavcodec.so'].avcodec_get_chroma_sub_sample
avcodec_get_chroma_sub_sample.restype = None
avcodec_get_chroma_sub_sample.argtypes = [PixelFormat, POINTER(c_int), POINTER(c_int)]
avcodec_pix_fmt_to_codec_tag = _libraries['/usr/local/lib/libavcodec.so'].avcodec_pix_fmt_to_codec_tag
avcodec_pix_fmt_to_codec_tag.restype = c_uint
avcodec_pix_fmt_to_codec_tag.argtypes = [PixelFormat]
avcodec_get_pix_fmt_loss = _libraries['/usr/local/lib/libavcodec.so'].avcodec_get_pix_fmt_loss
avcodec_get_pix_fmt_loss.restype = c_int
avcodec_get_pix_fmt_loss.argtypes = [PixelFormat, PixelFormat, c_int]
avcodec_find_best_pix_fmt = _libraries['/usr/local/lib/libavcodec.so'].avcodec_find_best_pix_fmt
avcodec_find_best_pix_fmt.restype = PixelFormat
avcodec_find_best_pix_fmt.argtypes = [int64_t, PixelFormat, c_int, POINTER(c_int)]
avcodec_find_best_pix_fmt2 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_find_best_pix_fmt2
avcodec_find_best_pix_fmt2.restype = PixelFormat
avcodec_find_best_pix_fmt2.argtypes = [PixelFormat, PixelFormat, PixelFormat, c_int, POINTER(c_int)]
avcodec_default_get_format = _libraries['/usr/local/lib/libavcodec.so'].avcodec_default_get_format
avcodec_default_get_format.restype = PixelFormat
avcodec_default_get_format.argtypes = [POINTER(AVCodecContext), POINTER(PixelFormat)]
avcodec_set_dimensions = _libraries['/usr/local/lib/libavcodec.so'].avcodec_set_dimensions
avcodec_set_dimensions.restype = None
avcodec_set_dimensions.argtypes = [POINTER(AVCodecContext), c_int, c_int]
av_get_codec_tag_string = _libraries['/usr/local/lib/libavcodec.so'].av_get_codec_tag_string
av_get_codec_tag_string.restype = size_t
av_get_codec_tag_string.argtypes = [STRING, size_t, c_uint]
avcodec_string = _libraries['/usr/local/lib/libavcodec.so'].avcodec_string
avcodec_string.restype = None
avcodec_string.argtypes = [STRING, c_int, POINTER(AVCodecContext), c_int]
av_get_profile_name = _libraries['/usr/local/lib/libavcodec.so'].av_get_profile_name
av_get_profile_name.restype = STRING
av_get_profile_name.argtypes = [POINTER(AVCodec), c_int]
avcodec_default_execute = _libraries['/usr/local/lib/libavcodec.so'].avcodec_default_execute
avcodec_default_execute.restype = c_int
avcodec_default_execute.argtypes = [POINTER(AVCodecContext), CFUNCTYPE(c_int, POINTER(AVCodecContext), c_void_p), c_void_p, POINTER(c_int), c_int, c_int]
avcodec_default_execute2 = _libraries['/usr/local/lib/libavcodec.so'].avcodec_default_execute2
avcodec_default_execute2.restype = c_int
avcodec_default_execute2.argtypes = [POINTER(AVCodecContext), CFUNCTYPE(c_int, POINTER(AVCodecContext), c_void_p, c_int, c_int), c_void_p, POINTER(c_int), c_int]
avcodec_fill_audio_frame = _libraries['/usr/local/lib/libavcodec.so'].avcodec_fill_audio_frame
avcodec_fill_audio_frame.restype = c_int
avcodec_fill_audio_frame.argtypes = [POINTER(AVFrame), c_int, AVSampleFormat, POINTER(uint8_t), c_int, c_int]
avcodec_flush_buffers = _libraries['/usr/local/lib/libavcodec.so'].avcodec_flush_buffers
avcodec_flush_buffers.restype = None
avcodec_flush_buffers.argtypes = [POINTER(AVCodecContext)]
avcodec_default_free_buffers = _libraries['/usr/local/lib/libavcodec.so'].avcodec_default_free_buffers
avcodec_default_free_buffers.restype = None
avcodec_default_free_buffers.argtypes = [POINTER(AVCodecContext)]
av_get_bits_per_sample = _libraries['/usr/local/lib/libavcodec.so'].av_get_bits_per_sample
av_get_bits_per_sample.restype = c_int
av_get_bits_per_sample.argtypes = [CodecID]
av_get_pcm_codec = _libraries['/usr/local/lib/libavcodec.so'].av_get_pcm_codec
av_get_pcm_codec.restype = CodecID
av_get_pcm_codec.argtypes = [AVSampleFormat, c_int]
av_get_exact_bits_per_sample = _libraries['/usr/local/lib/libavcodec.so'].av_get_exact_bits_per_sample
av_get_exact_bits_per_sample.restype = c_int
av_get_exact_bits_per_sample.argtypes = [CodecID]
av_get_audio_frame_duration = _libraries['/usr/local/lib/libavcodec.so'].av_get_audio_frame_duration
av_get_audio_frame_duration.restype = c_int
av_get_audio_frame_duration.argtypes = [POINTER(AVCodecContext), c_int]
class AVBitStreamFilterContext(Structure):
    pass
class AVBitStreamFilter(Structure):
    pass
AVBitStreamFilterContext._fields_ = [
    ('priv_data', c_void_p),
    ('filter', POINTER(AVBitStreamFilter)),
    ('parser', POINTER(AVCodecParserContext)),
    ('next', POINTER(AVBitStreamFilterContext)),
]
AVBitStreamFilter._fields_ = [
    ('name', STRING),
    ('priv_data_size', c_int),
    ('filter', CFUNCTYPE(c_int, POINTER(AVBitStreamFilterContext), POINTER(AVCodecContext), STRING, POINTER(POINTER(uint8_t)), POINTER(c_int), POINTER(uint8_t), c_int, c_int)),
    ('close', CFUNCTYPE(None, POINTER(AVBitStreamFilterContext))),
    ('next', POINTER(AVBitStreamFilter)),
]
av_register_bitstream_filter = _libraries['/usr/local/lib/libavcodec.so'].av_register_bitstream_filter
av_register_bitstream_filter.restype = None
av_register_bitstream_filter.argtypes = [POINTER(AVBitStreamFilter)]
av_bitstream_filter_init = _libraries['/usr/local/lib/libavcodec.so'].av_bitstream_filter_init
av_bitstream_filter_init.restype = POINTER(AVBitStreamFilterContext)
av_bitstream_filter_init.argtypes = [STRING]
av_bitstream_filter_filter = _libraries['/usr/local/lib/libavcodec.so'].av_bitstream_filter_filter
av_bitstream_filter_filter.restype = c_int
av_bitstream_filter_filter.argtypes = [POINTER(AVBitStreamFilterContext), POINTER(AVCodecContext), STRING, POINTER(POINTER(uint8_t)), POINTER(c_int), POINTER(uint8_t), c_int, c_int]
av_bitstream_filter_close = _libraries['/usr/local/lib/libavcodec.so'].av_bitstream_filter_close
av_bitstream_filter_close.restype = None
av_bitstream_filter_close.argtypes = [POINTER(AVBitStreamFilterContext)]
av_bitstream_filter_next = _libraries['/usr/local/lib/libavcodec.so'].av_bitstream_filter_next
av_bitstream_filter_next.restype = POINTER(AVBitStreamFilter)
av_bitstream_filter_next.argtypes = [POINTER(AVBitStreamFilter)]
av_fast_realloc = _libraries['/usr/local/lib/libavcodec.so'].av_fast_realloc
av_fast_realloc.restype = c_void_p
av_fast_realloc.argtypes = [c_void_p, POINTER(c_uint), size_t]
av_fast_malloc = _libraries['/usr/local/lib/libavcodec.so'].av_fast_malloc
av_fast_malloc.restype = None
av_fast_malloc.argtypes = [c_void_p, POINTER(c_uint), size_t]
av_fast_padded_malloc = _libraries['/usr/local/lib/libavcodec.so'].av_fast_padded_malloc
av_fast_padded_malloc.restype = None
av_fast_padded_malloc.argtypes = [c_void_p, POINTER(c_uint), size_t]
av_xiphlacing = _libraries['/usr/local/lib/libavcodec.so'].av_xiphlacing
av_xiphlacing.restype = c_uint
av_xiphlacing.argtypes = [POINTER(c_ubyte), c_uint]
av_log_missing_feature = _libraries['/usr/local/lib/libavcodec.so'].av_log_missing_feature
av_log_missing_feature.restype = None
av_log_missing_feature.argtypes = [c_void_p, STRING, c_int]
av_log_ask_for_sample = _libraries['/usr/local/lib/libavcodec.so'].av_log_ask_for_sample
av_log_ask_for_sample.restype = None
av_log_ask_for_sample.argtypes = [c_void_p, STRING]
av_register_hwaccel = _libraries['/usr/local/lib/libavcodec.so'].av_register_hwaccel
av_register_hwaccel.restype = None
av_register_hwaccel.argtypes = [POINTER(AVHWAccel)]
av_hwaccel_next = _libraries['/usr/local/lib/libavcodec.so'].av_hwaccel_next
av_hwaccel_next.restype = POINTER(AVHWAccel)
av_hwaccel_next.argtypes = [POINTER(AVHWAccel)]

# values for enumeration 'AVLockOp'
AVLockOp = c_int # enum
av_lockmgr_register = _libraries['/usr/local/lib/libavcodec.so'].av_lockmgr_register
av_lockmgr_register.restype = c_int
av_lockmgr_register.argtypes = [CFUNCTYPE(c_int, POINTER(c_void_p), AVLockOp)]
avcodec_get_type = _libraries['/usr/local/lib/libavcodec.so'].avcodec_get_type
avcodec_get_type.restype = AVMediaType
avcodec_get_type.argtypes = [CodecID]
avcodec_get_name = _libraries['/usr/local/lib/libavcodec.so'].avcodec_get_name
avcodec_get_name.restype = STRING
avcodec_get_name.argtypes = [CodecID]
avcodec_is_open = _libraries['/usr/local/lib/libavcodec.so'].avcodec_is_open
avcodec_is_open.restype = c_int
avcodec_is_open.argtypes = [POINTER(AVCodecContext)]
av_codec_is_encoder = _libraries['/usr/local/lib/libavcodec.so'].av_codec_is_encoder
av_codec_is_encoder.restype = c_int
av_codec_is_encoder.argtypes = [POINTER(AVCodec)]
av_codec_is_decoder = _libraries['/usr/local/lib/libavcodec.so'].av_codec_is_decoder
av_codec_is_decoder.restype = c_int
av_codec_is_decoder.argtypes = [POINTER(AVCodec)]
avdevice_version = _libraries['/usr/local/lib/libavdevice.so'].avdevice_version
avdevice_version.restype = c_uint
avdevice_version.argtypes = []
avdevice_configuration = _libraries['/usr/local/lib/libavdevice.so'].avdevice_configuration
avdevice_configuration.restype = STRING
avdevice_configuration.argtypes = []
avdevice_license = _libraries['/usr/local/lib/libavdevice.so'].avdevice_license
avdevice_license.restype = STRING
avdevice_license.argtypes = []
avdevice_register_all = _libraries['/usr/local/lib/libavdevice.so'].avdevice_register_all
avdevice_register_all.restype = None
avdevice_register_all.argtypes = []
avfilter_version = _libraries['/usr/local/lib/libavdevice.so'].avfilter_version
avfilter_version.restype = c_uint
avfilter_version.argtypes = []
avfilter_configuration = _libraries['/usr/local/lib/libavdevice.so'].avfilter_configuration
avfilter_configuration.restype = STRING
avfilter_configuration.argtypes = []
avfilter_license = _libraries['/usr/local/lib/libavdevice.so'].avfilter_license
avfilter_license.restype = STRING
avfilter_license.argtypes = []
class AVFilterContext(Structure):
    pass
class AVFilterLink(Structure):
    pass
class AVFilterPad(Structure):
    pass
class AVFilterFormats(Structure):
    pass
class AVFilterBuffer(Structure):
    pass
AVFilterBuffer._fields_ = [
    ('data', POINTER(uint8_t) * 8),
    ('linesize', c_int * 8),
    ('refcount', c_uint),
    ('priv', c_void_p),
    ('free', CFUNCTYPE(None, POINTER(AVFilterBuffer))),
    ('format', c_int),
    ('w', c_int),
    ('h', c_int),
    ('extended_data', POINTER(POINTER(uint8_t))),
]
class AVFilterBufferRefAudioProps(Structure):
    pass
AVFilterBufferRefAudioProps._fields_ = [
    ('channel_layout', uint64_t),
    ('nb_samples', c_int),
    ('sample_rate', c_int),
    ('planar', c_int),
]
class AVFilterBufferRefVideoProps(Structure):
    pass
AVFilterBufferRefVideoProps._fields_ = [
    ('w', c_int),
    ('h', c_int),
    ('sample_aspect_ratio', AVRational),
    ('interlaced', c_int),
    ('top_field_first', c_int),
    ('pict_type', AVPictureType),
    ('key_frame', c_int),
]
class AVFilterBufferRef(Structure):
    pass
AVFilterBufferRef._fields_ = [
    ('buf', POINTER(AVFilterBuffer)),
    ('data', POINTER(uint8_t) * 8),
    ('linesize', c_int * 8),
    ('format', c_int),
    ('pts', int64_t),
    ('pos', int64_t),
    ('perms', c_int),
    ('type', AVMediaType),
    ('video', POINTER(AVFilterBufferRefVideoProps)),
    ('audio', POINTER(AVFilterBufferRefAudioProps)),
    ('extended_data', POINTER(POINTER(uint8_t))),
]
avfilter_copy_buffer_ref_props = _libraries['/usr/local/lib/libavdevice.so'].avfilter_copy_buffer_ref_props
avfilter_copy_buffer_ref_props.restype = None
avfilter_copy_buffer_ref_props.argtypes = [POINTER(AVFilterBufferRef), POINTER(AVFilterBufferRef)]
avfilter_ref_buffer = _libraries['/usr/local/lib/libavdevice.so'].avfilter_ref_buffer
avfilter_ref_buffer.restype = POINTER(AVFilterBufferRef)
avfilter_ref_buffer.argtypes = [POINTER(AVFilterBufferRef), c_int]
avfilter_unref_buffer = _libraries['/usr/local/lib/libavdevice.so'].avfilter_unref_buffer
avfilter_unref_buffer.restype = None
avfilter_unref_buffer.argtypes = [POINTER(AVFilterBufferRef)]
avfilter_unref_bufferp = _libraries['/usr/local/lib/libavdevice.so'].avfilter_unref_bufferp
avfilter_unref_bufferp.restype = None
avfilter_unref_bufferp.argtypes = [POINTER(POINTER(AVFilterBufferRef))]
AVFilterFormats._fields_ = [
    ('format_count', c_uint),
    ('formats', POINTER(c_int)),
    ('refcount', c_uint),
    ('refs', POINTER(POINTER(POINTER(AVFilterFormats)))),
]
avfilter_make_format_list = _libraries['/usr/local/lib/libavdevice.so'].avfilter_make_format_list
avfilter_make_format_list.restype = POINTER(AVFilterFormats)
avfilter_make_format_list.argtypes = [POINTER(c_int)]
avfilter_add_format = _libraries['/usr/local/lib/libavdevice.so'].avfilter_add_format
avfilter_add_format.restype = c_int
avfilter_add_format.argtypes = [POINTER(POINTER(AVFilterFormats)), int64_t]
avfilter_all_formats = _libraries['/usr/local/lib/libavdevice.so'].avfilter_all_formats
avfilter_all_formats.restype = POINTER(AVFilterFormats)
avfilter_all_formats.argtypes = [AVMediaType]
avfilter_make_all_formats = _libraries['/usr/local/lib/libavdevice.so'].avfilter_make_all_formats
avfilter_make_all_formats.restype = POINTER(AVFilterFormats)
avfilter_make_all_formats.argtypes = [AVMediaType]
avfilter_all_channel_layouts = (int64_t * 0).in_dll(_libraries['/usr/local/lib/libavdevice.so'], 'avfilter_all_channel_layouts')
avfilter_make_all_packing_formats = _libraries['/usr/local/lib/libavdevice.so'].avfilter_make_all_packing_formats
avfilter_make_all_packing_formats.restype = POINTER(AVFilterFormats)
avfilter_make_all_packing_formats.argtypes = []
avfilter_merge_formats = _libraries['/usr/local/lib/libavdevice.so'].avfilter_merge_formats
avfilter_merge_formats.restype = POINTER(AVFilterFormats)
avfilter_merge_formats.argtypes = [POINTER(AVFilterFormats), POINTER(AVFilterFormats)]
avfilter_formats_ref = _libraries['/usr/local/lib/libavdevice.so'].avfilter_formats_ref
avfilter_formats_ref.restype = None
avfilter_formats_ref.argtypes = [POINTER(AVFilterFormats), POINTER(POINTER(AVFilterFormats))]
avfilter_formats_unref = _libraries['/usr/local/lib/libavdevice.so'].avfilter_formats_unref
avfilter_formats_unref.restype = None
avfilter_formats_unref.argtypes = [POINTER(POINTER(AVFilterFormats))]
avfilter_formats_changeref = _libraries['/usr/local/lib/libavdevice.so'].avfilter_formats_changeref
avfilter_formats_changeref.restype = None
avfilter_formats_changeref.argtypes = [POINTER(POINTER(AVFilterFormats)), POINTER(POINTER(AVFilterFormats))]
avfilter_set_common_formats = _libraries['/usr/local/lib/libavdevice.so'].avfilter_set_common_formats
avfilter_set_common_formats.restype = None
avfilter_set_common_formats.argtypes = [POINTER(AVFilterContext), POINTER(AVFilterFormats)]
avfilter_set_common_pixel_formats = _libraries['/usr/local/lib/libavdevice.so'].avfilter_set_common_pixel_formats
avfilter_set_common_pixel_formats.restype = None
avfilter_set_common_pixel_formats.argtypes = [POINTER(AVFilterContext), POINTER(AVFilterFormats)]
avfilter_set_common_sample_formats = _libraries['/usr/local/lib/libavdevice.so'].avfilter_set_common_sample_formats
avfilter_set_common_sample_formats.restype = None
avfilter_set_common_sample_formats.argtypes = [POINTER(AVFilterContext), POINTER(AVFilterFormats)]
avfilter_set_common_channel_layouts = _libraries['/usr/local/lib/libavdevice.so'].avfilter_set_common_channel_layouts
avfilter_set_common_channel_layouts.restype = None
avfilter_set_common_channel_layouts.argtypes = [POINTER(AVFilterContext), POINTER(AVFilterFormats)]
avfilter_set_common_packing_formats = _libraries['/usr/local/lib/libavdevice.so'].avfilter_set_common_packing_formats
avfilter_set_common_packing_formats.restype = None
avfilter_set_common_packing_formats.argtypes = [POINTER(AVFilterContext), POINTER(AVFilterFormats)]
AVFilterPad._fields_ = [
    ('name', STRING),
    ('type', AVMediaType),
    ('min_perms', c_int),
    ('rej_perms', c_int),
    ('start_frame', CFUNCTYPE(None, POINTER(AVFilterLink), POINTER(AVFilterBufferRef))),
    ('get_video_buffer', CFUNCTYPE(POINTER(AVFilterBufferRef), POINTER(AVFilterLink), c_int, c_int, c_int)),
    ('get_audio_buffer', CFUNCTYPE(POINTER(AVFilterBufferRef), POINTER(AVFilterLink), c_int, c_int)),
    ('end_frame', CFUNCTYPE(None, POINTER(AVFilterLink))),
    ('draw_slice', CFUNCTYPE(None, POINTER(AVFilterLink), c_int, c_int, c_int)),
    ('filter_samples', CFUNCTYPE(None, POINTER(AVFilterLink), POINTER(AVFilterBufferRef))),
    ('poll_frame', CFUNCTYPE(c_int, POINTER(AVFilterLink))),
    ('request_frame', CFUNCTYPE(c_int, POINTER(AVFilterLink))),
    ('config_props', CFUNCTYPE(c_int, POINTER(AVFilterLink))),
]
avfilter_pad_get_name = _libraries['/usr/local/lib/libavdevice.so'].avfilter_pad_get_name
avfilter_pad_get_name.restype = STRING
avfilter_pad_get_name.argtypes = [POINTER(AVFilterPad), c_int]
avfilter_pad_get_type = _libraries['/usr/local/lib/libavdevice.so'].avfilter_pad_get_type
avfilter_pad_get_type.restype = AVMediaType
avfilter_pad_get_type.argtypes = [POINTER(AVFilterPad), c_int]
avfilter_default_start_frame = _libraries['/usr/local/lib/libavdevice.so'].avfilter_default_start_frame
avfilter_default_start_frame.restype = None
avfilter_default_start_frame.argtypes = [POINTER(AVFilterLink), POINTER(AVFilterBufferRef)]
avfilter_default_draw_slice = _libraries['/usr/local/lib/libavdevice.so'].avfilter_default_draw_slice
avfilter_default_draw_slice.restype = None
avfilter_default_draw_slice.argtypes = [POINTER(AVFilterLink), c_int, c_int, c_int]
avfilter_default_end_frame = _libraries['/usr/local/lib/libavdevice.so'].avfilter_default_end_frame
avfilter_default_end_frame.restype = None
avfilter_default_end_frame.argtypes = [POINTER(AVFilterLink)]
avfilter_default_get_video_buffer = _libraries['/usr/local/lib/libavdevice.so'].avfilter_default_get_video_buffer
avfilter_default_get_video_buffer.restype = POINTER(AVFilterBufferRef)
avfilter_default_get_video_buffer.argtypes = [POINTER(AVFilterLink), c_int, c_int, c_int]
avfilter_default_query_formats = _libraries['/usr/local/lib/libavdevice.so'].avfilter_default_query_formats
avfilter_default_query_formats.restype = c_int
avfilter_default_query_formats.argtypes = [POINTER(AVFilterContext)]
avfilter_null_start_frame = _libraries['/usr/local/lib/libavdevice.so'].avfilter_null_start_frame
avfilter_null_start_frame.restype = None
avfilter_null_start_frame.argtypes = [POINTER(AVFilterLink), POINTER(AVFilterBufferRef)]
avfilter_null_draw_slice = _libraries['/usr/local/lib/libavdevice.so'].avfilter_null_draw_slice
avfilter_null_draw_slice.restype = None
avfilter_null_draw_slice.argtypes = [POINTER(AVFilterLink), c_int, c_int, c_int]
avfilter_null_end_frame = _libraries['/usr/local/lib/libavdevice.so'].avfilter_null_end_frame
avfilter_null_end_frame.restype = None
avfilter_null_end_frame.argtypes = [POINTER(AVFilterLink)]
avfilter_null_get_video_buffer = _libraries['/usr/local/lib/libavdevice.so'].avfilter_null_get_video_buffer
avfilter_null_get_video_buffer.restype = POINTER(AVFilterBufferRef)
avfilter_null_get_video_buffer.argtypes = [POINTER(AVFilterLink), c_int, c_int, c_int]
class AVFilter(Structure):
    pass
AVFilter._fields_ = [
    ('name', STRING),
    ('priv_size', c_int),
    ('init', CFUNCTYPE(c_int, POINTER(AVFilterContext), STRING, c_void_p)),
    ('uninit', CFUNCTYPE(None, POINTER(AVFilterContext))),
    ('query_formats', CFUNCTYPE(c_int, POINTER(AVFilterContext))),
    ('inputs', POINTER(AVFilterPad)),
    ('outputs', POINTER(AVFilterPad)),
    ('description', STRING),
    ('process_command', CFUNCTYPE(c_int, POINTER(AVFilterContext), STRING, STRING, STRING, c_int, c_int)),
]
class AVFilterCommand(Structure):
    pass
AVFilterContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('filter', POINTER(AVFilter)),
    ('name', STRING),
    ('input_count', c_uint),
    ('input_pads', POINTER(AVFilterPad)),
    ('inputs', POINTER(POINTER(AVFilterLink))),
    ('output_count', c_uint),
    ('output_pads', POINTER(AVFilterPad)),
    ('outputs', POINTER(POINTER(AVFilterLink))),
    ('priv', c_void_p),
    ('nb_inputs', c_uint),
    ('nb_outputs', c_uint),
    ('command_queue', POINTER(AVFilterCommand)),
]
AVFilterCommand._fields_ = [
]

# values for enumeration 'AVFilterPacking'
AVFilterPacking = c_int # enum

# values for unnamed enumeration
class AVFilterChannelLayouts(Structure):
    pass
class AVFilterPool(Structure):
    pass
class AVFilterGraph(Structure):
    pass
AVFilterLink._fields_ = [
    ('src', POINTER(AVFilterContext)),
    ('srcpad', POINTER(AVFilterPad)),
    ('dst', POINTER(AVFilterContext)),
    ('dstpad', POINTER(AVFilterPad)),
    ('init_state', c_int),
    ('type', AVMediaType),
    ('w', c_int),
    ('h', c_int),
    ('sample_aspect_ratio', AVRational),
    ('channel_layout', uint64_t),
    ('sample_rate', int64_t),
    ('planar', c_int),
    ('format', c_int),
    ('in_formats', POINTER(AVFilterFormats)),
    ('out_formats', POINTER(AVFilterFormats)),
    ('in_packing', POINTER(AVFilterFormats)),
    ('out_packing', POINTER(AVFilterFormats)),
    ('src_buf', POINTER(AVFilterBufferRef)),
    ('cur_buf', POINTER(AVFilterBufferRef)),
    ('out_buf', POINTER(AVFilterBufferRef)),
    ('time_base', AVRational),
    ('in_samplerates', POINTER(AVFilterFormats)),
    ('out_samplerates', POINTER(AVFilterFormats)),
    ('in_channel_layouts', POINTER(AVFilterChannelLayouts)),
    ('out_channel_layouts', POINTER(AVFilterChannelLayouts)),
    ('pool', POINTER(AVFilterPool)),
    ('graph', POINTER(AVFilterGraph)),
    ('current_pts', int64_t),
    ('age_index', c_int),
    ('frame_rate', AVRational),
]
AVFilterChannelLayouts._fields_ = [
]
AVFilterPool._fields_ = [
]
AVFilterGraph._fields_ = [
]
avfilter_link = _libraries['/usr/local/lib/libavdevice.so'].avfilter_link
avfilter_link.restype = c_int
avfilter_link.argtypes = [POINTER(AVFilterContext), c_uint, POINTER(AVFilterContext), c_uint]
avfilter_link_free = _libraries['/usr/local/lib/libavdevice.so'].avfilter_link_free
avfilter_link_free.restype = None
avfilter_link_free.argtypes = [POINTER(POINTER(AVFilterLink))]
avfilter_config_links = _libraries['/usr/local/lib/libavdevice.so'].avfilter_config_links
avfilter_config_links.restype = c_int
avfilter_config_links.argtypes = [POINTER(AVFilterContext)]
avfilter_get_video_buffer = _libraries['/usr/local/lib/libavdevice.so'].avfilter_get_video_buffer
avfilter_get_video_buffer.restype = POINTER(AVFilterBufferRef)
avfilter_get_video_buffer.argtypes = [POINTER(AVFilterLink), c_int, c_int, c_int]
avfilter_get_video_buffer_ref_from_arrays = _libraries['/usr/local/lib/libavdevice.so'].avfilter_get_video_buffer_ref_from_arrays
avfilter_get_video_buffer_ref_from_arrays.restype = POINTER(AVFilterBufferRef)
avfilter_get_video_buffer_ref_from_arrays.argtypes = [POINTER(POINTER(uint8_t)), POINTER(c_int), c_int, c_int, c_int, PixelFormat]
avfilter_get_audio_buffer_ref_from_arrays = _libraries['/usr/local/lib/libavdevice.so'].avfilter_get_audio_buffer_ref_from_arrays
avfilter_get_audio_buffer_ref_from_arrays.restype = POINTER(AVFilterBufferRef)
avfilter_get_audio_buffer_ref_from_arrays.argtypes = [POINTER(POINTER(uint8_t)), c_int, c_int, c_int, AVSampleFormat, uint64_t]
avfilter_request_frame = _libraries['/usr/local/lib/libavdevice.so'].avfilter_request_frame
avfilter_request_frame.restype = c_int
avfilter_request_frame.argtypes = [POINTER(AVFilterLink)]
avfilter_poll_frame = _libraries['/usr/local/lib/libavdevice.so'].avfilter_poll_frame
avfilter_poll_frame.restype = c_int
avfilter_poll_frame.argtypes = [POINTER(AVFilterLink)]
avfilter_start_frame = _libraries['/usr/local/lib/libavdevice.so'].avfilter_start_frame
avfilter_start_frame.restype = None
avfilter_start_frame.argtypes = [POINTER(AVFilterLink), POINTER(AVFilterBufferRef)]
avfilter_end_frame = _libraries['/usr/local/lib/libavdevice.so'].avfilter_end_frame
avfilter_end_frame.restype = None
avfilter_end_frame.argtypes = [POINTER(AVFilterLink)]
avfilter_draw_slice = _libraries['/usr/local/lib/libavdevice.so'].avfilter_draw_slice
avfilter_draw_slice.restype = None
avfilter_draw_slice.argtypes = [POINTER(AVFilterLink), c_int, c_int, c_int]
avfilter_process_command = _libraries['/usr/local/lib/libavdevice.so'].avfilter_process_command
avfilter_process_command.restype = c_int
avfilter_process_command.argtypes = [POINTER(AVFilterContext), STRING, STRING, STRING, c_int, c_int]
avfilter_register_all = _libraries['/usr/local/lib/libavdevice.so'].avfilter_register_all
avfilter_register_all.restype = None
avfilter_register_all.argtypes = []
avfilter_uninit = _libraries['/usr/local/lib/libavdevice.so'].avfilter_uninit
avfilter_uninit.restype = None
avfilter_uninit.argtypes = []
avfilter_register = _libraries['/usr/local/lib/libavdevice.so'].avfilter_register
avfilter_register.restype = c_int
avfilter_register.argtypes = [POINTER(AVFilter)]
avfilter_get_by_name = _libraries['/usr/local/lib/libavdevice.so'].avfilter_get_by_name
avfilter_get_by_name.restype = POINTER(AVFilter)
avfilter_get_by_name.argtypes = [STRING]
av_filter_next = _libraries['/usr/local/lib/libavdevice.so'].av_filter_next
av_filter_next.restype = POINTER(POINTER(AVFilter))
av_filter_next.argtypes = [POINTER(POINTER(AVFilter))]
avfilter_open = _libraries['/usr/local/lib/libavdevice.so'].avfilter_open
avfilter_open.restype = c_int
avfilter_open.argtypes = [POINTER(POINTER(AVFilterContext)), POINTER(AVFilter), STRING]
avfilter_init_filter = _libraries['/usr/local/lib/libavdevice.so'].avfilter_init_filter
avfilter_init_filter.restype = c_int
avfilter_init_filter.argtypes = [POINTER(AVFilterContext), STRING, c_void_p]
avfilter_free = _libraries['/usr/local/lib/libavdevice.so'].avfilter_free
avfilter_free.restype = None
avfilter_free.argtypes = [POINTER(AVFilterContext)]
avfilter_insert_filter = _libraries['/usr/local/lib/libavdevice.so'].avfilter_insert_filter
avfilter_insert_filter.restype = c_int
avfilter_insert_filter.argtypes = [POINTER(AVFilterLink), POINTER(AVFilterContext), c_uint, c_uint]
avfilter_insert_pad = _libraries['/usr/local/lib/libavdevice.so'].avfilter_insert_pad
avfilter_insert_pad.restype = None
avfilter_insert_pad.argtypes = [c_uint, POINTER(c_uint), size_t, POINTER(POINTER(AVFilterPad)), POINTER(POINTER(POINTER(AVFilterLink))), POINTER(AVFilterPad)]
avfilter_insert_inpad = _libraries['/usr/local/lib/libavdevice.so'].avfilter_insert_inpad
avfilter_insert_inpad.restype = None
avfilter_insert_inpad.argtypes = [POINTER(AVFilterContext), c_uint, POINTER(AVFilterPad)]
avfilter_insert_outpad = _libraries['/usr/local/lib/libavdevice.so'].avfilter_insert_outpad
avfilter_insert_outpad.restype = None
avfilter_insert_outpad.argtypes = [POINTER(AVFilterContext), c_uint, POINTER(AVFilterPad)]
class AVIOContext(Structure):
    pass
av_get_packet = _libraries['/usr/local/lib/libavformat.so'].av_get_packet
av_get_packet.restype = c_int
av_get_packet.argtypes = [POINTER(AVIOContext), POINTER(AVPacket), c_int]
av_append_packet = _libraries['/usr/local/lib/libavformat.so'].av_append_packet
av_append_packet.restype = c_int
av_append_packet.argtypes = [POINTER(AVIOContext), POINTER(AVPacket), c_int]
class AVFrac(Structure):
    pass
AVFrac._fields_ = [
    ('val', int64_t),
    ('num', int64_t),
    ('den', int64_t),
]
class AVCodecTag(Structure):
    pass
AVCodecTag._fields_ = [
]
class AVProbeData(Structure):
    pass
AVProbeData._fields_ = [
    ('filename', STRING),
    ('buf', POINTER(c_ubyte)),
    ('buf_size', c_int),
]
class AVOutputFormat(Structure):
    pass
class AVFormatContext(Structure):
    pass
AVOutputFormat._fields_ = [
    ('name', STRING),
    ('long_name', STRING),
    ('mime_type', STRING),
    ('extensions', STRING),
    ('audio_codec', CodecID),
    ('video_codec', CodecID),
    ('subtitle_codec', CodecID),
    ('flags', c_int),
    ('codec_tag', POINTER(POINTER(AVCodecTag))),
    ('priv_class', POINTER(AVClass)),
    ('next', POINTER(AVOutputFormat)),
    ('priv_data_size', c_int),
    ('write_header', CFUNCTYPE(c_int, POINTER(AVFormatContext))),
    ('write_packet', CFUNCTYPE(c_int, POINTER(AVFormatContext), POINTER(AVPacket))),
    ('write_trailer', CFUNCTYPE(c_int, POINTER(AVFormatContext))),
    ('interleave_packet', CFUNCTYPE(c_int, POINTER(AVFormatContext), POINTER(AVPacket), POINTER(AVPacket), c_int)),
    ('query_codec', CFUNCTYPE(c_int, CodecID, c_int)),
    ('get_output_timestamp', CFUNCTYPE(None, POINTER(AVFormatContext), c_int, POINTER(int64_t), POINTER(int64_t))),
]
class AVInputFormat(Structure):
    pass
AVInputFormat._fields_ = [
    ('name', STRING),
    ('long_name', STRING),
    ('flags', c_int),
    ('extensions', STRING),
    ('codec_tag', POINTER(POINTER(AVCodecTag))),
    ('priv_class', POINTER(AVClass)),
    ('next', POINTER(AVInputFormat)),
    ('raw_codec_id', c_int),
    ('priv_data_size', c_int),
    ('read_probe', CFUNCTYPE(c_int, POINTER(AVProbeData))),
    ('read_header', CFUNCTYPE(c_int, POINTER(AVFormatContext))),
    ('read_packet', CFUNCTYPE(c_int, POINTER(AVFormatContext), POINTER(AVPacket))),
    ('read_close', CFUNCTYPE(c_int, POINTER(AVFormatContext))),
    ('read_seek', CFUNCTYPE(c_int, POINTER(AVFormatContext), c_int, int64_t, c_int)),
    ('read_timestamp', CFUNCTYPE(int64_t, POINTER(AVFormatContext), c_int, POINTER(int64_t), int64_t)),
    ('read_play', CFUNCTYPE(c_int, POINTER(AVFormatContext))),
    ('read_pause', CFUNCTYPE(c_int, POINTER(AVFormatContext))),
    ('read_seek2', CFUNCTYPE(c_int, POINTER(AVFormatContext), c_int, int64_t, int64_t, int64_t, c_int)),
]

# values for enumeration 'AVStreamParseType'
AVStreamParseType = c_int # enum
class AVIndexEntry(Structure):
    pass
AVIndexEntry._fields_ = [
    ('pos', int64_t),
    ('timestamp', int64_t),
    ('flags', c_int, 2),
    ('size', c_int, 30),
    ('min_distance', c_int),
]
class AVStream(Structure):
    pass
class N8AVStream4DOT_34E(Structure):
    pass
class AVPacketList(Structure):
    pass
AVStream._fields_ = [
    ('index', c_int),
    ('id', c_int),
    ('codec', POINTER(AVCodecContext)),
    ('r_frame_rate', AVRational),
    ('priv_data', c_void_p),
    ('pts', AVFrac),
    ('time_base', AVRational),
    ('start_time', int64_t),
    ('duration', int64_t),
    ('nb_frames', int64_t),
    ('disposition', c_int),
    ('discard', AVDiscard),
    ('sample_aspect_ratio', AVRational),
    ('metadata', POINTER(AVDictionary)),
    ('avg_frame_rate', AVRational),
    ('attached_pic', AVPacket),
    ('info', POINTER(N8AVStream4DOT_34E)),
    ('pts_wrap_bits', c_int),
    ('reference_dts', int64_t),
    ('first_dts', int64_t),
    ('cur_dts', int64_t),
    ('last_IP_pts', int64_t),
    ('last_IP_duration', c_int),
    ('probe_packets', c_int),
    ('codec_info_nb_frames', c_int),
    ('stream_identifier', c_int),
    ('interleaver_chunk_size', int64_t),
    ('interleaver_chunk_duration', int64_t),
    ('need_parsing', AVStreamParseType),
    ('parser', POINTER(AVCodecParserContext)),
    ('last_in_packet_buffer', POINTER(AVPacketList)),
    ('probe_data', AVProbeData),
    ('pts_buffer', int64_t * 17),
    ('index_entries', POINTER(AVIndexEntry)),
    ('nb_index_entries', c_int),
    ('index_entries_allocated_size', c_uint),
    ('request_probe', c_int),
    ('skip_to_keyframe', c_int),
]
N8AVStream4DOT_34E._fields_ = [
    ('last_dts', int64_t),
    ('duration_gcd', int64_t),
    ('duration_count', c_int),
    ('duration_error', c_double * 726 * 2 * 2),
    ('codec_info_duration', int64_t),
    ('nb_decoded_frames', c_int),
    ('found_decoder', c_int),
]
class AVProgram(Structure):
    pass
AVProgram._fields_ = [
    ('id', c_int),
    ('flags', c_int),
    ('discard', AVDiscard),
    ('stream_index', POINTER(c_uint)),
    ('nb_stream_indexes', c_uint),
    ('metadata', POINTER(AVDictionary)),
    ('program_num', c_int),
    ('pmt_pid', c_int),
    ('pcr_pid', c_int),
]
class AVChapter(Structure):
    pass
AVChapter._fields_ = [
    ('id', c_int),
    ('time_base', AVRational),
    ('start', int64_t),
    ('end', int64_t),
    ('metadata', POINTER(AVDictionary)),
]
class AVIOInterruptCB(Structure):
    pass
AVIOInterruptCB._fields_ = [
    ('callback', CFUNCTYPE(c_int, c_void_p)),
    ('opaque', c_void_p),
]

# values for unnamed enumeration
AVFormatContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('iformat', POINTER(AVInputFormat)),
    ('oformat', POINTER(AVOutputFormat)),
    ('priv_data', c_void_p),
    ('pb', POINTER(AVIOContext)),
    ('ctx_flags', c_int),
    ('nb_streams', c_uint),
    ('streams', POINTER(POINTER(AVStream))),
    ('filename', c_char * 1024),
    ('start_time', int64_t),
    ('duration', int64_t),
    ('bit_rate', c_int),
    ('packet_size', c_uint),
    ('max_delay', c_int),
    ('flags', c_int),
    ('probesize', c_uint),
    ('max_analyze_duration', c_int),
    ('key', POINTER(uint8_t)),
    ('keylen', c_int),
    ('nb_programs', c_uint),
    ('programs', POINTER(POINTER(AVProgram))),
    ('video_codec_id', CodecID),
    ('audio_codec_id', CodecID),
    ('subtitle_codec_id', CodecID),
    ('max_index_size', c_uint),
    ('max_picture_buffer', c_uint),
    ('nb_chapters', c_uint),
    ('chapters', POINTER(POINTER(AVChapter))),
    ('metadata', POINTER(AVDictionary)),
    ('start_time_realtime', int64_t),
    ('fps_probe_size', c_int),
    ('error_recognition', c_int),
    ('interrupt_callback', AVIOInterruptCB),
    ('debug', c_int),
    ('ts_id', c_int),
    ('audio_preload', c_int),
    ('max_chunk_duration', c_int),
    ('max_chunk_size', c_int),
    ('packet_buffer', POINTER(AVPacketList)),
    ('packet_buffer_end', POINTER(AVPacketList)),
    ('data_offset', int64_t),
    ('raw_packet_buffer', POINTER(AVPacketList)),
    ('raw_packet_buffer_end', POINTER(AVPacketList)),
    ('parse_queue', POINTER(AVPacketList)),
    ('parse_queue_end', POINTER(AVPacketList)),
    ('raw_packet_buffer_remaining_size', c_int),
    ('avio_flags', c_int),
    ('duration_estimation_method', c_int),
]
av_fmt_ctx_get_duration_estimation_method = _libraries['/usr/local/lib/libavformat.so'].av_fmt_ctx_get_duration_estimation_method
av_fmt_ctx_get_duration_estimation_method.restype = c_int
av_fmt_ctx_get_duration_estimation_method.argtypes = [POINTER(AVFormatContext)]
AVPacketList._fields_ = [
    ('pkt', AVPacket),
    ('next', POINTER(AVPacketList)),
]
avformat_version = _libraries['/usr/local/lib/libavformat.so'].avformat_version
avformat_version.restype = c_uint
avformat_version.argtypes = []
avformat_configuration = _libraries['/usr/local/lib/libavformat.so'].avformat_configuration
avformat_configuration.restype = STRING
avformat_configuration.argtypes = []
avformat_license = _libraries['/usr/local/lib/libavformat.so'].avformat_license
avformat_license.restype = STRING
avformat_license.argtypes = []
av_register_all = _libraries['/usr/local/lib/libavformat.so'].av_register_all
av_register_all.restype = None
av_register_all.argtypes = []
av_register_input_format = _libraries['/usr/local/lib/libavformat.so'].av_register_input_format
av_register_input_format.restype = None
av_register_input_format.argtypes = [POINTER(AVInputFormat)]
av_register_output_format = _libraries['/usr/local/lib/libavformat.so'].av_register_output_format
av_register_output_format.restype = None
av_register_output_format.argtypes = [POINTER(AVOutputFormat)]
avformat_network_init = _libraries['/usr/local/lib/libavformat.so'].avformat_network_init
avformat_network_init.restype = c_int
avformat_network_init.argtypes = []
avformat_network_deinit = _libraries['/usr/local/lib/libavformat.so'].avformat_network_deinit
avformat_network_deinit.restype = c_int
avformat_network_deinit.argtypes = []
av_iformat_next = _libraries['/usr/local/lib/libavformat.so'].av_iformat_next
av_iformat_next.restype = POINTER(AVInputFormat)
av_iformat_next.argtypes = [POINTER(AVInputFormat)]
av_oformat_next = _libraries['/usr/local/lib/libavformat.so'].av_oformat_next
av_oformat_next.restype = POINTER(AVOutputFormat)
av_oformat_next.argtypes = [POINTER(AVOutputFormat)]
avformat_alloc_context = _libraries['/usr/local/lib/libavformat.so'].avformat_alloc_context
avformat_alloc_context.restype = POINTER(AVFormatContext)
avformat_alloc_context.argtypes = []
avformat_free_context = _libraries['/usr/local/lib/libavformat.so'].avformat_free_context
avformat_free_context.restype = None
avformat_free_context.argtypes = [POINTER(AVFormatContext)]
avformat_get_class = _libraries['/usr/local/lib/libavformat.so'].avformat_get_class
avformat_get_class.restype = POINTER(AVClass)
avformat_get_class.argtypes = []
avformat_new_stream = _libraries['/usr/local/lib/libavformat.so'].avformat_new_stream
avformat_new_stream.restype = POINTER(AVStream)
avformat_new_stream.argtypes = [POINTER(AVFormatContext), POINTER(AVCodec)]
av_new_program = _libraries['/usr/local/lib/libavformat.so'].av_new_program
av_new_program.restype = POINTER(AVProgram)
av_new_program.argtypes = [POINTER(AVFormatContext), c_int]
avformat_alloc_output_context = _libraries['/usr/local/lib/libavformat.so'].avformat_alloc_output_context
avformat_alloc_output_context.restype = POINTER(AVFormatContext)
avformat_alloc_output_context.argtypes = [STRING, POINTER(AVOutputFormat), STRING]
avformat_alloc_output_context2 = _libraries['/usr/local/lib/libavformat.so'].avformat_alloc_output_context2
avformat_alloc_output_context2.restype = c_int
avformat_alloc_output_context2.argtypes = [POINTER(POINTER(AVFormatContext)), POINTER(AVOutputFormat), STRING, STRING]
av_find_input_format = _libraries['/usr/local/lib/libavformat.so'].av_find_input_format
av_find_input_format.restype = POINTER(AVInputFormat)
av_find_input_format.argtypes = [STRING]
av_probe_input_format = _libraries['/usr/local/lib/libavformat.so'].av_probe_input_format
av_probe_input_format.restype = POINTER(AVInputFormat)
av_probe_input_format.argtypes = [POINTER(AVProbeData), c_int]
av_probe_input_format2 = _libraries['/usr/local/lib/libavformat.so'].av_probe_input_format2
av_probe_input_format2.restype = POINTER(AVInputFormat)
av_probe_input_format2.argtypes = [POINTER(AVProbeData), c_int, POINTER(c_int)]
av_probe_input_format3 = _libraries['/usr/local/lib/libavformat.so'].av_probe_input_format3
av_probe_input_format3.restype = POINTER(AVInputFormat)
av_probe_input_format3.argtypes = [POINTER(AVProbeData), c_int, POINTER(c_int)]
av_probe_input_buffer = _libraries['/usr/local/lib/libavformat.so'].av_probe_input_buffer
av_probe_input_buffer.restype = c_int
av_probe_input_buffer.argtypes = [POINTER(AVIOContext), POINTER(POINTER(AVInputFormat)), STRING, c_void_p, c_uint, c_uint]
avformat_open_input = _libraries['/usr/local/lib/libavformat.so'].avformat_open_input
avformat_open_input.restype = c_int
avformat_open_input.argtypes = [POINTER(POINTER(AVFormatContext)), STRING, POINTER(AVInputFormat), POINTER(POINTER(AVDictionary))]
av_demuxer_open = _libraries['/usr/local/lib/libavformat.so'].av_demuxer_open
av_demuxer_open.restype = c_int
av_demuxer_open.argtypes = [POINTER(AVFormatContext)]
av_find_stream_info = _libraries['/usr/local/lib/libavformat.so'].av_find_stream_info
av_find_stream_info.restype = c_int
av_find_stream_info.argtypes = [POINTER(AVFormatContext)]
avformat_find_stream_info = _libraries['/usr/local/lib/libavformat.so'].avformat_find_stream_info
avformat_find_stream_info.restype = c_int
avformat_find_stream_info.argtypes = [POINTER(AVFormatContext), POINTER(POINTER(AVDictionary))]
av_find_program_from_stream = _libraries['/usr/local/lib/libavformat.so'].av_find_program_from_stream
av_find_program_from_stream.restype = POINTER(AVProgram)
av_find_program_from_stream.argtypes = [POINTER(AVFormatContext), POINTER(AVProgram), c_int]
av_find_best_stream = _libraries['/usr/local/lib/libavformat.so'].av_find_best_stream
av_find_best_stream.restype = c_int
av_find_best_stream.argtypes = [POINTER(AVFormatContext), AVMediaType, c_int, c_int, POINTER(POINTER(AVCodec)), c_int]
av_read_packet = _libraries['/usr/local/lib/libavformat.so'].av_read_packet
av_read_packet.restype = c_int
av_read_packet.argtypes = [POINTER(AVFormatContext), POINTER(AVPacket)]
av_read_frame = _libraries['/usr/local/lib/libavformat.so'].av_read_frame
av_read_frame.restype = c_int
av_read_frame.argtypes = [POINTER(AVFormatContext), POINTER(AVPacket)]
av_seek_frame = _libraries['/usr/local/lib/libavformat.so'].av_seek_frame
av_seek_frame.restype = c_int
av_seek_frame.argtypes = [POINTER(AVFormatContext), c_int, int64_t, c_int]
avformat_seek_file = _libraries['/usr/local/lib/libavformat.so'].avformat_seek_file
avformat_seek_file.restype = c_int
avformat_seek_file.argtypes = [POINTER(AVFormatContext), c_int, int64_t, int64_t, int64_t, c_int]
av_read_play = _libraries['/usr/local/lib/libavformat.so'].av_read_play
av_read_play.restype = c_int
av_read_play.argtypes = [POINTER(AVFormatContext)]
av_read_pause = _libraries['/usr/local/lib/libavformat.so'].av_read_pause
av_read_pause.restype = c_int
av_read_pause.argtypes = [POINTER(AVFormatContext)]
av_close_input_file = _libraries['/usr/local/lib/libavformat.so'].av_close_input_file
av_close_input_file.restype = None
av_close_input_file.argtypes = [POINTER(AVFormatContext)]
avformat_close_input = _libraries['/usr/local/lib/libavformat.so'].avformat_close_input
avformat_close_input.restype = None
avformat_close_input.argtypes = [POINTER(POINTER(AVFormatContext))]
av_new_stream = _libraries['/usr/local/lib/libavformat.so'].av_new_stream
av_new_stream.restype = POINTER(AVStream)
av_new_stream.argtypes = [POINTER(AVFormatContext), c_int]
av_set_pts_info = _libraries['/usr/local/lib/libavformat.so'].av_set_pts_info
av_set_pts_info.restype = None
av_set_pts_info.argtypes = [POINTER(AVStream), c_int, c_uint, c_uint]
avformat_write_header = _libraries['/usr/local/lib/libavformat.so'].avformat_write_header
avformat_write_header.restype = c_int
avformat_write_header.argtypes = [POINTER(AVFormatContext), POINTER(POINTER(AVDictionary))]
av_write_frame = _libraries['/usr/local/lib/libavformat.so'].av_write_frame
av_write_frame.restype = c_int
av_write_frame.argtypes = [POINTER(AVFormatContext), POINTER(AVPacket)]
av_interleaved_write_frame = _libraries['/usr/local/lib/libavformat.so'].av_interleaved_write_frame
av_interleaved_write_frame.restype = c_int
av_interleaved_write_frame.argtypes = [POINTER(AVFormatContext), POINTER(AVPacket)]
av_interleave_packet_per_dts = _libraries['/usr/local/lib/libavformat.so'].av_interleave_packet_per_dts
av_interleave_packet_per_dts.restype = c_int
av_interleave_packet_per_dts.argtypes = [POINTER(AVFormatContext), POINTER(AVPacket), POINTER(AVPacket), c_int]
av_write_trailer = _libraries['/usr/local/lib/libavformat.so'].av_write_trailer
av_write_trailer.restype = c_int
av_write_trailer.argtypes = [POINTER(AVFormatContext)]
av_guess_format = _libraries['/usr/local/lib/libavformat.so'].av_guess_format
av_guess_format.restype = POINTER(AVOutputFormat)
av_guess_format.argtypes = [STRING, STRING, STRING]
av_guess_codec = _libraries['/usr/local/lib/libavformat.so'].av_guess_codec
av_guess_codec.restype = CodecID
av_guess_codec.argtypes = [POINTER(AVOutputFormat), STRING, STRING, STRING, AVMediaType]
av_get_output_timestamp = _libraries['/usr/local/lib/libavformat.so'].av_get_output_timestamp
av_get_output_timestamp.restype = c_int
av_get_output_timestamp.argtypes = [POINTER(AVFormatContext), c_int, POINTER(int64_t), POINTER(int64_t)]
FILE = _IO_FILE
av_hex_dump = _libraries['/usr/local/lib/libavformat.so'].av_hex_dump
av_hex_dump.restype = None
av_hex_dump.argtypes = [POINTER(FILE), POINTER(uint8_t), c_int]
av_hex_dump_log = _libraries['/usr/local/lib/libavformat.so'].av_hex_dump_log
av_hex_dump_log.restype = None
av_hex_dump_log.argtypes = [c_void_p, c_int, POINTER(uint8_t), c_int]
av_pkt_dump2 = _libraries['/usr/local/lib/libavformat.so'].av_pkt_dump2
av_pkt_dump2.restype = None
av_pkt_dump2.argtypes = [POINTER(FILE), POINTER(AVPacket), c_int, POINTER(AVStream)]
av_pkt_dump_log2 = _libraries['/usr/local/lib/libavformat.so'].av_pkt_dump_log2
av_pkt_dump_log2.restype = None
av_pkt_dump_log2.argtypes = [c_void_p, c_int, POINTER(AVPacket), c_int, POINTER(AVStream)]
av_codec_get_id = _libraries['/usr/local/lib/libavformat.so'].av_codec_get_id
av_codec_get_id.restype = CodecID
av_codec_get_id.argtypes = [POINTER(POINTER(AVCodecTag)), c_uint]
av_codec_get_tag = _libraries['/usr/local/lib/libavformat.so'].av_codec_get_tag
av_codec_get_tag.restype = c_uint
av_codec_get_tag.argtypes = [POINTER(POINTER(AVCodecTag)), CodecID]
av_find_default_stream_index = _libraries['/usr/local/lib/libavformat.so'].av_find_default_stream_index
av_find_default_stream_index.restype = c_int
av_find_default_stream_index.argtypes = [POINTER(AVFormatContext)]
av_index_search_timestamp = _libraries['/usr/local/lib/libavformat.so'].av_index_search_timestamp
av_index_search_timestamp.restype = c_int
av_index_search_timestamp.argtypes = [POINTER(AVStream), int64_t, c_int]
av_add_index_entry = _libraries['/usr/local/lib/libavformat.so'].av_add_index_entry
av_add_index_entry.restype = c_int
av_add_index_entry.argtypes = [POINTER(AVStream), int64_t, int64_t, c_int, c_int, c_int]
av_url_split = _libraries['/usr/local/lib/libavformat.so'].av_url_split
av_url_split.restype = None
av_url_split.argtypes = [STRING, c_int, STRING, c_int, STRING, c_int, POINTER(c_int), STRING, c_int, STRING]
av_dump_format = _libraries['/usr/local/lib/libavformat.so'].av_dump_format
av_dump_format.restype = None
av_dump_format.argtypes = [POINTER(AVFormatContext), c_int, STRING, c_int]
av_gettime = _libraries['/usr/local/lib/libavcodec.so'].av_gettime
av_gettime.restype = int64_t
av_gettime.argtypes = []
av_get_frame_filename = _libraries['/usr/local/lib/libavformat.so'].av_get_frame_filename
av_get_frame_filename.restype = c_int
av_get_frame_filename.argtypes = [STRING, c_int, STRING, c_int]
av_filename_number_test = _libraries['/usr/local/lib/libavformat.so'].av_filename_number_test
av_filename_number_test.restype = c_int
av_filename_number_test.argtypes = [STRING]
av_sdp_create = _libraries['/usr/local/lib/libavformat.so'].av_sdp_create
av_sdp_create.restype = c_int
av_sdp_create.argtypes = [POINTER(POINTER(AVFormatContext)), c_int, STRING, c_int]
av_match_ext = _libraries['/usr/local/lib/libavformat.so'].av_match_ext
av_match_ext.restype = c_int
av_match_ext.argtypes = [STRING, STRING]
avformat_query_codec = _libraries['/usr/local/lib/libavformat.so'].avformat_query_codec
avformat_query_codec.restype = c_int
avformat_query_codec.argtypes = [POINTER(AVOutputFormat), CodecID, c_int]
avformat_get_riff_video_tags = _libraries['/usr/local/lib/libavformat.so'].avformat_get_riff_video_tags
avformat_get_riff_video_tags.restype = POINTER(AVCodecTag)
avformat_get_riff_video_tags.argtypes = []
avformat_get_riff_audio_tags = _libraries['/usr/local/lib/libavformat.so'].avformat_get_riff_audio_tags
avformat_get_riff_audio_tags.restype = POINTER(AVCodecTag)
avformat_get_riff_audio_tags.argtypes = []
av_guess_sample_aspect_ratio = _libraries['/usr/local/lib/libavformat.so'].av_guess_sample_aspect_ratio
av_guess_sample_aspect_ratio.restype = AVRational
av_guess_sample_aspect_ratio.argtypes = [POINTER(AVFormatContext), POINTER(AVStream), POINTER(AVFrame)]
AVIOContext._fields_ = [
    ('av_class', POINTER(AVClass)),
    ('buffer', POINTER(c_ubyte)),
    ('buffer_size', c_int),
    ('buf_ptr', POINTER(c_ubyte)),
    ('buf_end', POINTER(c_ubyte)),
    ('opaque', c_void_p),
    ('read_packet', CFUNCTYPE(c_int, c_void_p, POINTER(uint8_t), c_int)),
    ('write_packet', CFUNCTYPE(c_int, c_void_p, POINTER(uint8_t), c_int)),
    ('seek', CFUNCTYPE(int64_t, c_void_p, int64_t, c_int)),
    ('pos', int64_t),
    ('must_flush', c_int),
    ('eof_reached', c_int),
    ('write_flag', c_int),
    ('max_packet_size', c_int),
    ('checksum', c_ulong),
    ('checksum_ptr', POINTER(c_ubyte)),
    ('update_checksum', CFUNCTYPE(c_ulong, c_ulong, POINTER(uint8_t), c_uint)),
    ('error', c_int),
    ('read_pause', CFUNCTYPE(c_int, c_void_p, c_int)),
    ('read_seek', CFUNCTYPE(int64_t, c_void_p, c_int, int64_t, c_int)),
    ('seekable', c_int),
    ('maxsize', int64_t),
    ('direct', c_int),
    ('bytes_read', int64_t),
    ('seek_count', c_int),
]
avio_check = _libraries['/usr/local/lib/libavformat.so'].avio_check
avio_check.restype = c_int
avio_check.argtypes = [STRING, c_int]
avio_alloc_context = _libraries['/usr/local/lib/libavformat.so'].avio_alloc_context
avio_alloc_context.restype = POINTER(AVIOContext)
avio_alloc_context.argtypes = [POINTER(c_ubyte), c_int, c_int, c_void_p, CFUNCTYPE(c_int, c_void_p, POINTER(uint8_t), c_int), CFUNCTYPE(c_int, c_void_p, POINTER(uint8_t), c_int), CFUNCTYPE(int64_t, c_void_p, int64_t, c_int)]
avio_w8 = _libraries['/usr/local/lib/libavformat.so'].avio_w8
avio_w8.restype = None
avio_w8.argtypes = [POINTER(AVIOContext), c_int]
avio_write = _libraries['/usr/local/lib/libavformat.so'].avio_write
avio_write.restype = None
avio_write.argtypes = [POINTER(AVIOContext), POINTER(c_ubyte), c_int]
avio_wl64 = _libraries['/usr/local/lib/libavformat.so'].avio_wl64
avio_wl64.restype = None
avio_wl64.argtypes = [POINTER(AVIOContext), uint64_t]
avio_wb64 = _libraries['/usr/local/lib/libavformat.so'].avio_wb64
avio_wb64.restype = None
avio_wb64.argtypes = [POINTER(AVIOContext), uint64_t]
avio_wl32 = _libraries['/usr/local/lib/libavformat.so'].avio_wl32
avio_wl32.restype = None
avio_wl32.argtypes = [POINTER(AVIOContext), c_uint]
avio_wb32 = _libraries['/usr/local/lib/libavformat.so'].avio_wb32
avio_wb32.restype = None
avio_wb32.argtypes = [POINTER(AVIOContext), c_uint]
avio_wl24 = _libraries['/usr/local/lib/libavformat.so'].avio_wl24
avio_wl24.restype = None
avio_wl24.argtypes = [POINTER(AVIOContext), c_uint]
avio_wb24 = _libraries['/usr/local/lib/libavformat.so'].avio_wb24
avio_wb24.restype = None
avio_wb24.argtypes = [POINTER(AVIOContext), c_uint]
avio_wl16 = _libraries['/usr/local/lib/libavformat.so'].avio_wl16
avio_wl16.restype = None
avio_wl16.argtypes = [POINTER(AVIOContext), c_uint]
avio_wb16 = _libraries['/usr/local/lib/libavformat.so'].avio_wb16
avio_wb16.restype = None
avio_wb16.argtypes = [POINTER(AVIOContext), c_uint]
avio_put_str = _libraries['/usr/local/lib/libavformat.so'].avio_put_str
avio_put_str.restype = c_int
avio_put_str.argtypes = [POINTER(AVIOContext), STRING]
avio_put_str16le = _libraries['/usr/local/lib/libavformat.so'].avio_put_str16le
avio_put_str16le.restype = c_int
avio_put_str16le.argtypes = [POINTER(AVIOContext), STRING]
avio_seek = _libraries['/usr/local/lib/libavformat.so'].avio_seek
avio_seek.restype = int64_t
avio_seek.argtypes = [POINTER(AVIOContext), int64_t, c_int]
avio_skip = _libraries['/usr/local/lib/libavformat.so'].avio_skip
avio_skip.restype = int64_t
avio_skip.argtypes = [POINTER(AVIOContext), int64_t]
avio_size = _libraries['/usr/local/lib/libavformat.so'].avio_size
avio_size.restype = int64_t
avio_size.argtypes = [POINTER(AVIOContext)]
url_feof = _libraries['/usr/local/lib/libavformat.so'].url_feof
url_feof.restype = c_int
url_feof.argtypes = [POINTER(AVIOContext)]
avio_printf = _libraries['/usr/local/lib/libavformat.so'].avio_printf
avio_printf.restype = c_int
avio_printf.argtypes = [POINTER(AVIOContext), STRING]
avio_flush = _libraries['/usr/local/lib/libavformat.so'].avio_flush
avio_flush.restype = None
avio_flush.argtypes = [POINTER(AVIOContext)]
avio_read = _libraries['/usr/local/lib/libavformat.so'].avio_read
avio_read.restype = c_int
avio_read.argtypes = [POINTER(AVIOContext), POINTER(c_ubyte), c_int]
avio_r8 = _libraries['/usr/local/lib/libavformat.so'].avio_r8
avio_r8.restype = c_int
avio_r8.argtypes = [POINTER(AVIOContext)]
avio_rl16 = _libraries['/usr/local/lib/libavformat.so'].avio_rl16
avio_rl16.restype = c_uint
avio_rl16.argtypes = [POINTER(AVIOContext)]
avio_rl24 = _libraries['/usr/local/lib/libavformat.so'].avio_rl24
avio_rl24.restype = c_uint
avio_rl24.argtypes = [POINTER(AVIOContext)]
avio_rl32 = _libraries['/usr/local/lib/libavformat.so'].avio_rl32
avio_rl32.restype = c_uint
avio_rl32.argtypes = [POINTER(AVIOContext)]
avio_rl64 = _libraries['/usr/local/lib/libavformat.so'].avio_rl64
avio_rl64.restype = uint64_t
avio_rl64.argtypes = [POINTER(AVIOContext)]
avio_rb16 = _libraries['/usr/local/lib/libavformat.so'].avio_rb16
avio_rb16.restype = c_uint
avio_rb16.argtypes = [POINTER(AVIOContext)]
avio_rb24 = _libraries['/usr/local/lib/libavformat.so'].avio_rb24
avio_rb24.restype = c_uint
avio_rb24.argtypes = [POINTER(AVIOContext)]
avio_rb32 = _libraries['/usr/local/lib/libavformat.so'].avio_rb32
avio_rb32.restype = c_uint
avio_rb32.argtypes = [POINTER(AVIOContext)]
avio_rb64 = _libraries['/usr/local/lib/libavformat.so'].avio_rb64
avio_rb64.restype = uint64_t
avio_rb64.argtypes = [POINTER(AVIOContext)]
avio_get_str = _libraries['/usr/local/lib/libavformat.so'].avio_get_str
avio_get_str.restype = c_int
avio_get_str.argtypes = [POINTER(AVIOContext), c_int, STRING, c_int]
avio_get_str16le = _libraries['/usr/local/lib/libavformat.so'].avio_get_str16le
avio_get_str16le.restype = c_int
avio_get_str16le.argtypes = [POINTER(AVIOContext), c_int, STRING, c_int]
avio_get_str16be = _libraries['/usr/local/lib/libavformat.so'].avio_get_str16be
avio_get_str16be.restype = c_int
avio_get_str16be.argtypes = [POINTER(AVIOContext), c_int, STRING, c_int]
avio_open = _libraries['/usr/local/lib/libavformat.so'].avio_open
avio_open.restype = c_int
avio_open.argtypes = [POINTER(POINTER(AVIOContext)), STRING, c_int]
avio_open2 = _libraries['/usr/local/lib/libavformat.so'].avio_open2
avio_open2.restype = c_int
avio_open2.argtypes = [POINTER(POINTER(AVIOContext)), STRING, c_int, POINTER(AVIOInterruptCB), POINTER(POINTER(AVDictionary))]
avio_close = _libraries['/usr/local/lib/libavformat.so'].avio_close
avio_close.restype = c_int
avio_close.argtypes = [POINTER(AVIOContext)]
avio_open_dyn_buf = _libraries['/usr/local/lib/libavformat.so'].avio_open_dyn_buf
avio_open_dyn_buf.restype = c_int
avio_open_dyn_buf.argtypes = [POINTER(POINTER(AVIOContext))]
avio_close_dyn_buf = _libraries['/usr/local/lib/libavformat.so'].avio_close_dyn_buf
avio_close_dyn_buf.restype = c_int
avio_close_dyn_buf.argtypes = [POINTER(AVIOContext), POINTER(POINTER(uint8_t))]
avio_enum_protocols = _libraries['/usr/local/lib/libavformat.so'].avio_enum_protocols
avio_enum_protocols.restype = STRING
avio_enum_protocols.argtypes = [POINTER(c_void_p), c_int]
avio_pause = _libraries['/usr/local/lib/libavformat.so'].avio_pause
avio_pause.restype = c_int
avio_pause.argtypes = [POINTER(AVIOContext), c_int]
avio_seek_time = _libraries['/usr/local/lib/libavformat.so'].avio_seek_time
avio_seek_time.restype = int64_t
avio_seek_time.argtypes = [POINTER(AVIOContext), c_int, int64_t, c_int]

# values for enumeration 'AVMatrixEncoding'
AVMatrixEncoding = c_int # enum
av_get_channel_layout = _libraries['/usr/local/lib/libavcodec.so'].av_get_channel_layout
av_get_channel_layout.restype = uint64_t
av_get_channel_layout.argtypes = [STRING]
av_get_channel_layout_string = _libraries['/usr/local/lib/libavcodec.so'].av_get_channel_layout_string
av_get_channel_layout_string.restype = None
av_get_channel_layout_string.argtypes = [STRING, c_int, c_int, uint64_t]
class AVBPrint(Structure):
    pass
AVBPrint._fields_ = [
]
av_bprint_channel_layout = _libraries['/usr/local/lib/libavcodec.so'].av_bprint_channel_layout
av_bprint_channel_layout.restype = None
av_bprint_channel_layout.argtypes = [POINTER(AVBPrint), c_int, uint64_t]
av_get_channel_layout_nb_channels = _libraries['/usr/local/lib/libavcodec.so'].av_get_channel_layout_nb_channels
av_get_channel_layout_nb_channels.restype = c_int
av_get_channel_layout_nb_channels.argtypes = [uint64_t]
av_get_default_channel_layout = _libraries['/usr/local/lib/libavcodec.so'].av_get_default_channel_layout
av_get_default_channel_layout.restype = int64_t
av_get_default_channel_layout.argtypes = [c_int]
av_get_channel_layout_channel_index = _libraries['/usr/local/lib/libavcodec.so'].av_get_channel_layout_channel_index
av_get_channel_layout_channel_index.restype = c_int
av_get_channel_layout_channel_index.argtypes = [uint64_t, uint64_t]
av_channel_layout_extract_channel = _libraries['/usr/local/lib/libavcodec.so'].av_channel_layout_extract_channel
av_channel_layout_extract_channel.restype = uint64_t
av_channel_layout_extract_channel.argtypes = [uint64_t, c_int]
av_get_channel_name = _libraries['/usr/local/lib/libavcodec.so'].av_get_channel_name
av_get_channel_name.restype = STRING
av_get_channel_name.argtypes = [uint64_t]
avutil_version = _libraries['/usr/local/lib/libavcodec.so'].avutil_version
avutil_version.restype = c_uint
avutil_version.argtypes = []
avutil_configuration = _libraries['/usr/local/lib/libavcodec.so'].avutil_configuration
avutil_configuration.restype = STRING
avutil_configuration.argtypes = []
avutil_license = _libraries['/usr/local/lib/libavcodec.so'].avutil_license
avutil_license.restype = STRING
avutil_license.argtypes = []
av_get_media_type_string = _libraries['/usr/local/lib/libavcodec.so'].av_get_media_type_string
av_get_media_type_string.restype = STRING
av_get_media_type_string.argtypes = [AVMediaType]
av_get_picture_type_char = _libraries['/usr/local/lib/libavcodec.so'].av_get_picture_type_char
av_get_picture_type_char.restype = c_char
av_get_picture_type_char.argtypes = [AVPictureType]
ff_log2_tab = (uint8_t * 256).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'ff_log2_tab')
av_reverse = (uint8_t * 256).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'av_reverse')
av_get_cpu_flags = _libraries['/usr/local/lib/libavcodec.so'].av_get_cpu_flags
av_get_cpu_flags.restype = c_int
av_get_cpu_flags.argtypes = []
av_force_cpu_flags = _libraries['/usr/local/lib/libavcodec.so'].av_force_cpu_flags
av_force_cpu_flags.restype = None
av_force_cpu_flags.argtypes = [c_int]
av_set_cpu_flags_mask = _libraries['/usr/local/lib/libavcodec.so'].av_set_cpu_flags_mask
av_set_cpu_flags_mask.restype = None
av_set_cpu_flags_mask.argtypes = [c_int]
av_parse_cpu_flags = _libraries['/usr/local/lib/libavcodec.so'].av_parse_cpu_flags
av_parse_cpu_flags.restype = c_int
av_parse_cpu_flags.argtypes = [STRING]
av_parse_cpu_caps = _libraries['/usr/local/lib/libavcodec.so'].av_parse_cpu_caps
av_parse_cpu_caps.restype = c_int
av_parse_cpu_caps.argtypes = [POINTER(c_uint), STRING]
ff_get_cpu_flags_x86 = _libraries['/usr/local/lib/libavcodec.so'].ff_get_cpu_flags_x86
ff_get_cpu_flags_x86.restype = c_int
ff_get_cpu_flags_x86.argtypes = []
class AVDictionaryEntry(Structure):
    pass
AVDictionaryEntry._fields_ = [
    ('key', STRING),
    ('value', STRING),
]
AVDictionary._fields_ = [
]
av_dict_get = _libraries['/usr/local/lib/libavcodec.so'].av_dict_get
av_dict_get.restype = POINTER(AVDictionaryEntry)
av_dict_get.argtypes = [POINTER(AVDictionary), STRING, POINTER(AVDictionaryEntry), c_int]
av_dict_set = _libraries['/usr/local/lib/libavcodec.so'].av_dict_set
av_dict_set.restype = c_int
av_dict_set.argtypes = [POINTER(POINTER(AVDictionary)), STRING, STRING, c_int]
av_dict_copy = _libraries['/usr/local/lib/libavcodec.so'].av_dict_copy
av_dict_copy.restype = None
av_dict_copy.argtypes = [POINTER(POINTER(AVDictionary)), POINTER(AVDictionary), c_int]
av_dict_free = _libraries['/usr/local/lib/libavcodec.so'].av_dict_free
av_dict_free.restype = None
av_dict_free.argtypes = [POINTER(POINTER(AVDictionary))]
av_strerror = _libraries['/usr/local/lib/libavcodec.so'].av_strerror
av_strerror.restype = c_int
av_strerror.argtypes = [c_int, STRING, size_t]
class AVExtFloat(Structure):
    pass
AVExtFloat._fields_ = [
    ('exponent', uint8_t * 2),
    ('mantissa', uint8_t * 8),
]
av_int2dbl = _libraries['/usr/local/lib/libavcodec.so'].av_int2dbl
av_int2dbl.restype = c_double
av_int2dbl.argtypes = [int64_t]
int32_t = c_int32
av_int2flt = _libraries['/usr/local/lib/libavcodec.so'].av_int2flt
av_int2flt.restype = c_float
av_int2flt.argtypes = [int32_t]
av_ext2dbl = _libraries['/usr/local/lib/libavcodec.so'].av_ext2dbl
av_ext2dbl.restype = c_double
av_ext2dbl.argtypes = [AVExtFloat]
av_dbl2int = _libraries['/usr/local/lib/libavcodec.so'].av_dbl2int
av_dbl2int.restype = int64_t
av_dbl2int.argtypes = [c_double]
av_flt2int = _libraries['/usr/local/lib/libavcodec.so'].av_flt2int
av_flt2int.restype = int32_t
av_flt2int.argtypes = [c_float]
av_dbl2ext = _libraries['/usr/local/lib/libavcodec.so'].av_dbl2ext
av_dbl2ext.restype = AVExtFloat
av_dbl2ext.argtypes = [c_double]

# values for enumeration 'AVClassCategory'
AVClassCategory = c_int # enum
class AVOption(Structure):
    pass
AVOption._fields_ = [
]
AVClass._fields_ = [
    ('class_name', STRING),
    ('item_name', CFUNCTYPE(STRING, c_void_p)),
    ('option', POINTER(AVOption)),
    ('version', c_int),
    ('log_level_offset_offset', c_int),
    ('parent_log_context_offset', c_int),
    ('child_next', CFUNCTYPE(c_void_p, c_void_p, c_void_p)),
    ('child_class_next', CFUNCTYPE(POINTER(AVClass), POINTER(AVClass))),
    ('category', AVClassCategory),
    ('get_category', CFUNCTYPE(AVClassCategory, c_void_p)),
]
av_log = _libraries['/usr/local/lib/libavcodec.so'].av_log
av_log.restype = None
av_log.argtypes = [c_void_p, c_int, STRING]
av_vlog = _libraries['/usr/local/lib/libavcodec.so'].av_vlog
av_vlog.restype = None
av_vlog.argtypes = [c_void_p, c_int, STRING, POINTER(__va_list_tag)]
av_log_get_level = _libraries['/usr/local/lib/libavcodec.so'].av_log_get_level
av_log_get_level.restype = c_int
av_log_get_level.argtypes = []
av_log_set_level = _libraries['/usr/local/lib/libavcodec.so'].av_log_set_level
av_log_set_level.restype = None
av_log_set_level.argtypes = [c_int]
av_log_set_callback = _libraries['/usr/local/lib/libavcodec.so'].av_log_set_callback
av_log_set_callback.restype = None
av_log_set_callback.argtypes = [CFUNCTYPE(None, c_void_p, c_int, STRING, POINTER(__va_list_tag))]
av_log_default_callback = _libraries['/usr/local/lib/libavcodec.so'].av_log_default_callback
av_log_default_callback.restype = None
av_log_default_callback.argtypes = [c_void_p, c_int, STRING, POINTER(__va_list_tag)]
av_default_item_name = _libraries['/usr/local/lib/libavcodec.so'].av_default_item_name
av_default_item_name.restype = STRING
av_default_item_name.argtypes = [c_void_p]
av_default_get_category = _libraries['/usr/local/lib/libavcodec.so'].av_default_get_category
av_default_get_category.restype = AVClassCategory
av_default_get_category.argtypes = [c_void_p]
av_log_format_line = _libraries['/usr/local/lib/libavcodec.so'].av_log_format_line
av_log_format_line.restype = None
av_log_format_line.argtypes = [c_void_p, c_int, STRING, POINTER(__va_list_tag), STRING, c_int, POINTER(c_int)]
av_log_set_flags = _libraries['/usr/local/lib/libavcodec.so'].av_log_set_flags
av_log_set_flags.restype = None
av_log_set_flags.argtypes = [c_int]

# values for enumeration 'AVRounding'
AVRounding = c_int # enum
av_gcd = _libraries['/usr/local/lib/libavcodec.so'].av_gcd
av_gcd.restype = int64_t
av_gcd.argtypes = [int64_t, int64_t]
av_rescale = _libraries['/usr/local/lib/libavcodec.so'].av_rescale
av_rescale.restype = int64_t
av_rescale.argtypes = [int64_t, int64_t, int64_t]
av_rescale_rnd = _libraries['/usr/local/lib/libavcodec.so'].av_rescale_rnd
av_rescale_rnd.restype = int64_t
av_rescale_rnd.argtypes = [int64_t, int64_t, int64_t, AVRounding]
av_rescale_q = _libraries['/usr/local/lib/libavcodec.so'].av_rescale_q
av_rescale_q.restype = int64_t
av_rescale_q.argtypes = [int64_t, AVRational, AVRational]
av_rescale_q_rnd = _libraries['/usr/local/lib/libavcodec.so'].av_rescale_q_rnd
av_rescale_q_rnd.restype = int64_t
av_rescale_q_rnd.argtypes = [int64_t, AVRational, AVRational, AVRounding]
av_compare_ts = _libraries['/usr/local/lib/libavcodec.so'].av_compare_ts
av_compare_ts.restype = c_int
av_compare_ts.argtypes = [int64_t, AVRational, int64_t, AVRational]
av_compare_mod = _libraries['/usr/local/lib/libavcodec.so'].av_compare_mod
av_compare_mod.restype = int64_t
av_compare_mod.argtypes = [uint64_t, uint64_t, uint64_t]
av_malloc = _libraries['/usr/local/lib/libavcodec.so'].av_malloc
av_malloc.restype = c_void_p
av_malloc.argtypes = [size_t]
av_realloc = _libraries['/usr/local/lib/libavcodec.so'].av_realloc
av_realloc.restype = c_void_p
av_realloc.argtypes = [c_void_p, size_t]
av_realloc_f = _libraries['/usr/local/lib/libavcodec.so'].av_realloc_f
av_realloc_f.restype = c_void_p
av_realloc_f.argtypes = [c_void_p, size_t, size_t]
av_free = _libraries['/usr/local/lib/libavcodec.so'].av_free
av_free.restype = None
av_free.argtypes = [c_void_p]
av_mallocz = _libraries['/usr/local/lib/libavcodec.so'].av_mallocz
av_mallocz.restype = c_void_p
av_mallocz.argtypes = [size_t]
av_calloc = _libraries['/usr/local/lib/libavcodec.so'].av_calloc
av_calloc.restype = c_void_p
av_calloc.argtypes = [size_t, size_t]
av_strdup = _libraries['/usr/local/lib/libavcodec.so'].av_strdup
av_strdup.restype = STRING
av_strdup.argtypes = [STRING]
av_freep = _libraries['/usr/local/lib/libavcodec.so'].av_freep
av_freep.restype = None
av_freep.argtypes = [c_void_p]
av_dynarray_add = _libraries['/usr/local/lib/libavcodec.so'].av_dynarray_add
av_dynarray_add.restype = None
av_dynarray_add.argtypes = [c_void_p, POINTER(c_int), c_void_p]
av_max_alloc = _libraries['/usr/local/lib/libavcodec.so'].av_max_alloc
av_max_alloc.restype = None
av_max_alloc.argtypes = [size_t]
av_reduce = _libraries['/usr/local/lib/libavcodec.so'].av_reduce
av_reduce.restype = c_int
av_reduce.argtypes = [POINTER(c_int), POINTER(c_int), int64_t, int64_t, int64_t]
av_mul_q = _libraries['/usr/local/lib/libavcodec.so'].av_mul_q
av_mul_q.restype = AVRational
av_mul_q.argtypes = [AVRational, AVRational]
av_div_q = _libraries['/usr/local/lib/libavcodec.so'].av_div_q
av_div_q.restype = AVRational
av_div_q.argtypes = [AVRational, AVRational]
av_add_q = _libraries['/usr/local/lib/libavcodec.so'].av_add_q
av_add_q.restype = AVRational
av_add_q.argtypes = [AVRational, AVRational]
av_sub_q = _libraries['/usr/local/lib/libavcodec.so'].av_sub_q
av_sub_q.restype = AVRational
av_sub_q.argtypes = [AVRational, AVRational]
av_d2q = _libraries['/usr/local/lib/libavcodec.so'].av_d2q
av_d2q.restype = AVRational
av_d2q.argtypes = [c_double, c_int]
av_nearer_q = _libraries['/usr/local/lib/libavcodec.so'].av_nearer_q
av_nearer_q.restype = c_int
av_nearer_q.argtypes = [AVRational, AVRational, AVRational]
av_find_nearest_q_idx = _libraries['/usr/local/lib/libavcodec.so'].av_find_nearest_q_idx
av_find_nearest_q_idx.restype = c_int
av_find_nearest_q_idx.argtypes = [AVRational, POINTER(AVRational)]
av_get_sample_fmt_name = _libraries['/usr/local/lib/libavcodec.so'].av_get_sample_fmt_name
av_get_sample_fmt_name.restype = STRING
av_get_sample_fmt_name.argtypes = [AVSampleFormat]
av_get_sample_fmt = _libraries['/usr/local/lib/libavcodec.so'].av_get_sample_fmt
av_get_sample_fmt.restype = AVSampleFormat
av_get_sample_fmt.argtypes = [STRING]
av_get_alt_sample_fmt = _libraries['/usr/local/lib/libavcodec.so'].av_get_alt_sample_fmt
av_get_alt_sample_fmt.restype = AVSampleFormat
av_get_alt_sample_fmt.argtypes = [AVSampleFormat, c_int]
av_get_packed_sample_fmt = _libraries['/usr/local/lib/libavcodec.so'].av_get_packed_sample_fmt
av_get_packed_sample_fmt.restype = AVSampleFormat
av_get_packed_sample_fmt.argtypes = [AVSampleFormat]
av_get_planar_sample_fmt = _libraries['/usr/local/lib/libavcodec.so'].av_get_planar_sample_fmt
av_get_planar_sample_fmt.restype = AVSampleFormat
av_get_planar_sample_fmt.argtypes = [AVSampleFormat]
av_get_sample_fmt_string = _libraries['/usr/local/lib/libavcodec.so'].av_get_sample_fmt_string
av_get_sample_fmt_string.restype = STRING
av_get_sample_fmt_string.argtypes = [STRING, c_int, AVSampleFormat]
av_get_bits_per_sample_fmt = _libraries['/usr/local/lib/libavcodec.so'].av_get_bits_per_sample_fmt
av_get_bits_per_sample_fmt.restype = c_int
av_get_bits_per_sample_fmt.argtypes = [AVSampleFormat]
av_get_bytes_per_sample = _libraries['/usr/local/lib/libavcodec.so'].av_get_bytes_per_sample
av_get_bytes_per_sample.restype = c_int
av_get_bytes_per_sample.argtypes = [AVSampleFormat]
av_sample_fmt_is_planar = _libraries['/usr/local/lib/libavcodec.so'].av_sample_fmt_is_planar
av_sample_fmt_is_planar.restype = c_int
av_sample_fmt_is_planar.argtypes = [AVSampleFormat]
av_samples_get_buffer_size = _libraries['/usr/local/lib/libavcodec.so'].av_samples_get_buffer_size
av_samples_get_buffer_size.restype = c_int
av_samples_get_buffer_size.argtypes = [POINTER(c_int), c_int, c_int, AVSampleFormat, c_int]
av_samples_fill_arrays = _libraries['/usr/local/lib/libavcodec.so'].av_samples_fill_arrays
av_samples_fill_arrays.restype = c_int
av_samples_fill_arrays.argtypes = [POINTER(POINTER(uint8_t)), POINTER(c_int), POINTER(uint8_t), c_int, c_int, AVSampleFormat, c_int]
av_samples_alloc = _libraries['/usr/local/lib/libavcodec.so'].av_samples_alloc
av_samples_alloc.restype = c_int
av_samples_alloc.argtypes = [POINTER(POINTER(uint8_t)), POINTER(c_int), c_int, c_int, AVSampleFormat, c_int]
av_samples_copy = _libraries['/usr/local/lib/libavcodec.so'].av_samples_copy
av_samples_copy.restype = c_int
av_samples_copy.argtypes = [POINTER(POINTER(uint8_t)), POINTER(POINTER(uint8_t)), c_int, c_int, c_int, c_int, AVSampleFormat]
av_samples_set_silence = _libraries['/usr/local/lib/libavcodec.so'].av_samples_set_silence
av_samples_set_silence.restype = c_int
av_samples_set_silence.argtypes = [POINTER(POINTER(uint8_t)), c_int, c_int, c_int, AVSampleFormat]
postproc_version = _libraries['/usr/local/lib/libavdevice.so'].postproc_version
postproc_version.restype = c_uint
postproc_version.argtypes = []
postproc_configuration = _libraries['/usr/local/lib/libavdevice.so'].postproc_configuration
postproc_configuration.restype = STRING
postproc_configuration.argtypes = []
postproc_license = _libraries['/usr/local/lib/libavdevice.so'].postproc_license
postproc_license.restype = STRING
postproc_license.argtypes = []
pp_context = None
pp_mode = None
pp_help = (c_char * 0).in_dll(_libraries['/usr/local/lib/libavdevice.so'], 'pp_help')
pp_postprocess = _libraries['/usr/local/lib/libavdevice.so'].pp_postprocess
pp_postprocess.restype = None
pp_postprocess.argtypes = [POINTER(POINTER(uint8_t)), POINTER(c_int), POINTER(POINTER(uint8_t)), POINTER(c_int), c_int, c_int, POINTER(int8_t), c_int, POINTER(pp_mode), POINTER(pp_context), c_int]
pp_get_mode_by_name_and_quality = _libraries['/usr/local/lib/libavdevice.so'].pp_get_mode_by_name_and_quality
pp_get_mode_by_name_and_quality.restype = POINTER(pp_mode)
pp_get_mode_by_name_and_quality.argtypes = [STRING, c_int]
pp_free_mode = _libraries['/usr/local/lib/libavdevice.so'].pp_free_mode
pp_free_mode.restype = None
pp_free_mode.argtypes = [POINTER(pp_mode)]
pp_get_context = _libraries['/usr/local/lib/libavdevice.so'].pp_get_context
pp_get_context.restype = POINTER(pp_context)
pp_get_context.argtypes = [c_int, c_int, c_int]
pp_free_context = _libraries['/usr/local/lib/libavdevice.so'].pp_free_context
pp_free_context.restype = None
pp_free_context.argtypes = [POINTER(pp_context)]
swscale_version = _libraries['/usr/local/lib/libswscale.so'].swscale_version
swscale_version.restype = c_uint
swscale_version.argtypes = []
swscale_configuration = _libraries['/usr/local/lib/libswscale.so'].swscale_configuration
swscale_configuration.restype = STRING
swscale_configuration.argtypes = []
swscale_license = _libraries['/usr/local/lib/libswscale.so'].swscale_license
swscale_license.restype = STRING
swscale_license.argtypes = []
sws_getCoefficients = _libraries['/usr/local/lib/libswscale.so'].sws_getCoefficients
sws_getCoefficients.restype = POINTER(c_int)
sws_getCoefficients.argtypes = [c_int]
class SwsVector(Structure):
    pass
SwsVector._fields_ = [
    ('coeff', POINTER(c_double)),
    ('length', c_int),
]
class SwsFilter(Structure):
    pass
SwsFilter._fields_ = [
    ('lumH', POINTER(SwsVector)),
    ('lumV', POINTER(SwsVector)),
    ('chrH', POINTER(SwsVector)),
    ('chrV', POINTER(SwsVector)),
]
class SwsContext(Structure):
    pass
SwsContext._fields_ = [
]
sws_isSupportedInput = _libraries['/usr/local/lib/libswscale.so'].sws_isSupportedInput
sws_isSupportedInput.restype = c_int
sws_isSupportedInput.argtypes = [PixelFormat]
sws_isSupportedOutput = _libraries['/usr/local/lib/libswscale.so'].sws_isSupportedOutput
sws_isSupportedOutput.restype = c_int
sws_isSupportedOutput.argtypes = [PixelFormat]
sws_alloc_context = _libraries['/usr/local/lib/libswscale.so'].sws_alloc_context
sws_alloc_context.restype = POINTER(SwsContext)
sws_alloc_context.argtypes = []
sws_init_context = _libraries['/usr/local/lib/libswscale.so'].sws_init_context
sws_init_context.restype = c_int
sws_init_context.argtypes = [POINTER(SwsContext), POINTER(SwsFilter), POINTER(SwsFilter)]
sws_freeContext = _libraries['/usr/local/lib/libswscale.so'].sws_freeContext
sws_freeContext.restype = None
sws_freeContext.argtypes = [POINTER(SwsContext)]
sws_getContext = _libraries['/usr/local/lib/libswscale.so'].sws_getContext
sws_getContext.restype = POINTER(SwsContext)
sws_getContext.argtypes = [c_int, c_int, PixelFormat, c_int, c_int, PixelFormat, c_int, POINTER(SwsFilter), POINTER(SwsFilter), POINTER(c_double)]
sws_scale = _libraries['/usr/local/lib/libswscale.so'].sws_scale
sws_scale.restype = c_int
sws_scale.argtypes = [POINTER(SwsContext), POINTER(POINTER(uint8_t)), POINTER(c_int), c_int, c_int, POINTER(POINTER(uint8_t)), POINTER(c_int)]
sws_setColorspaceDetails = _libraries['/usr/local/lib/libswscale.so'].sws_setColorspaceDetails
sws_setColorspaceDetails.restype = c_int
sws_setColorspaceDetails.argtypes = [POINTER(SwsContext), POINTER(c_int), c_int, POINTER(c_int), c_int, c_int, c_int, c_int]
sws_getColorspaceDetails = _libraries['/usr/local/lib/libswscale.so'].sws_getColorspaceDetails
sws_getColorspaceDetails.restype = c_int
sws_getColorspaceDetails.argtypes = [POINTER(SwsContext), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
sws_allocVec = _libraries['/usr/local/lib/libswscale.so'].sws_allocVec
sws_allocVec.restype = POINTER(SwsVector)
sws_allocVec.argtypes = [c_int]
sws_getGaussianVec = _libraries['/usr/local/lib/libswscale.so'].sws_getGaussianVec
sws_getGaussianVec.restype = POINTER(SwsVector)
sws_getGaussianVec.argtypes = [c_double, c_double]
sws_getConstVec = _libraries['/usr/local/lib/libswscale.so'].sws_getConstVec
sws_getConstVec.restype = POINTER(SwsVector)
sws_getConstVec.argtypes = [c_double, c_int]
sws_getIdentityVec = _libraries['/usr/local/lib/libswscale.so'].sws_getIdentityVec
sws_getIdentityVec.restype = POINTER(SwsVector)
sws_getIdentityVec.argtypes = []
sws_scaleVec = _libraries['/usr/local/lib/libswscale.so'].sws_scaleVec
sws_scaleVec.restype = None
sws_scaleVec.argtypes = [POINTER(SwsVector), c_double]
sws_normalizeVec = _libraries['/usr/local/lib/libswscale.so'].sws_normalizeVec
sws_normalizeVec.restype = None
sws_normalizeVec.argtypes = [POINTER(SwsVector), c_double]
sws_convVec = _libraries['/usr/local/lib/libswscale.so'].sws_convVec
sws_convVec.restype = None
sws_convVec.argtypes = [POINTER(SwsVector), POINTER(SwsVector)]
sws_addVec = _libraries['/usr/local/lib/libswscale.so'].sws_addVec
sws_addVec.restype = None
sws_addVec.argtypes = [POINTER(SwsVector), POINTER(SwsVector)]
sws_subVec = _libraries['/usr/local/lib/libswscale.so'].sws_subVec
sws_subVec.restype = None
sws_subVec.argtypes = [POINTER(SwsVector), POINTER(SwsVector)]
sws_shiftVec = _libraries['/usr/local/lib/libswscale.so'].sws_shiftVec
sws_shiftVec.restype = None
sws_shiftVec.argtypes = [POINTER(SwsVector), c_int]
sws_cloneVec = _libraries['/usr/local/lib/libswscale.so'].sws_cloneVec
sws_cloneVec.restype = POINTER(SwsVector)
sws_cloneVec.argtypes = [POINTER(SwsVector)]
sws_printVec2 = _libraries['/usr/local/lib/libswscale.so'].sws_printVec2
sws_printVec2.restype = None
sws_printVec2.argtypes = [POINTER(SwsVector), POINTER(AVClass), c_int]
sws_freeVec = _libraries['/usr/local/lib/libswscale.so'].sws_freeVec
sws_freeVec.restype = None
sws_freeVec.argtypes = [POINTER(SwsVector)]
sws_getDefaultFilter = _libraries['/usr/local/lib/libswscale.so'].sws_getDefaultFilter
sws_getDefaultFilter.restype = POINTER(SwsFilter)
sws_getDefaultFilter.argtypes = [c_float, c_float, c_float, c_float, c_float, c_float, c_int]
sws_freeFilter = _libraries['/usr/local/lib/libswscale.so'].sws_freeFilter
sws_freeFilter.restype = None
sws_freeFilter.argtypes = [POINTER(SwsFilter)]
sws_getCachedContext = _libraries['/usr/local/lib/libswscale.so'].sws_getCachedContext
sws_getCachedContext.restype = POINTER(SwsContext)
sws_getCachedContext.argtypes = [POINTER(SwsContext), c_int, c_int, PixelFormat, c_int, c_int, PixelFormat, c_int, POINTER(SwsFilter), POINTER(SwsFilter), POINTER(c_double)]
sws_convertPalette8ToPacked32 = _libraries['/usr/local/lib/libswscale.so'].sws_convertPalette8ToPacked32
sws_convertPalette8ToPacked32.restype = None
sws_convertPalette8ToPacked32.argtypes = [POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t)]
sws_convertPalette8ToPacked24 = _libraries['/usr/local/lib/libswscale.so'].sws_convertPalette8ToPacked24
sws_convertPalette8ToPacked24.restype = None
sws_convertPalette8ToPacked24.argtypes = [POINTER(uint8_t), POINTER(uint8_t), c_int, POINTER(uint8_t)]
sws_get_class = _libraries['/usr/local/lib/libswscale.so'].sws_get_class
sws_get_class.restype = POINTER(AVClass)
sws_get_class.argtypes = []
LIBAVCODEC_VERSION_MAJOR = 54 # Variable c_int '54'
FF_IDCT_BINK = 24 # Variable c_int '24'
FF_THREAD_SLICE = 2 # Variable c_int '2'
ETXTBSY = 26 # Variable c_int '26'
EOF = -1 # Variable c_int '-0x00000000000000001'
math_errhandling = 3 # Variable c_int '3'
ETOOMANYREFS = 109 # Variable c_int '109'
_MATH_H = 1 # Variable c_int '1'
FF_CODER_TYPE_VLC = 0 # Variable c_int '0'
AVFMT_NOBINSEARCH = 8192 # Variable c_int '8192'
_IO_USER_LOCK = 32768 # Variable c_int '32768'
LONG_MIN = -9223372036854775808 # Variable c_long '-0x08000000000000000l'
AV_CPU_FLAG_SSE = 8 # Variable c_int '8'
MAX_STD_TIMEBASES = 726 # Variable c_int '726'
ENAMETOOLONG = 36 # Variable c_int '36'
ENOPKG = 65 # Variable c_int '65'
AV_CH_LAYOUT_OCTAGONAL = 1847 # Variable c_int '1847'
USHRT_MAX = 65535 # Variable c_int '65535'
AVERROR_EOF = -541478725 # Variable c_int '-0x00000000020464f45'
FF_IDCT_EA = 21 # Variable c_int '21'
LIBAVFORMAT_VERSION_MAJOR = 54 # Variable c_int '54'
__WCOREFLAG = 128 # Variable c_int '128'
FF_PROFILE_H264_HIGH_10 = 110 # Variable c_int '110'
_G_HAVE_MREMAP = 1 # Variable c_int '1'
AV_CPU_FLAG_ARMV6 = 2 # Variable c_int '2'
CODEC_FLAG_AC_PRED = 16777216 # Variable c_int '16777216'
FF_PROFILE_AAC_LOW = 1 # Variable c_int '1'
_IO_EOF_SEEN = 16 # Variable c_int '16'
EINPROGRESS = 115 # Variable c_int '115'
L_cuserid = 9 # Variable c_int '9'
ENOTSOCK = 88 # Variable c_int '88'
AVPALETTE_COUNT = 256 # Variable c_int '256'
AV_CH_WIDE_RIGHT = 4294967296L # Variable c_ulonglong '4294967296ull'
AV_CH_LAYOUT_SURROUND = 7 # Variable c_int '7'
CODEC_FLAG2_DROP_FRAME_TIMECODE = 8192 # Variable c_int '8192'
AVFILTER_CMD_FLAG_FAST = 2 # Variable c_int '2'
FF_PROFILE_H264_CAVLC_444 = 44 # Variable c_int '44'
AV_DISPOSITION_HEARING_IMPAIRED = 128 # Variable c_int '128'
FF_BUFFER_HINTS_PRESERVE = 4 # Variable c_int '4'
FF_DCT_FASTINT = 1 # Variable c_int '1'
MB_TYPE_P0L0 = 4096 # Variable c_int '4096'
EFBIG = 27 # Variable c_int '27'
AV_LOG_WARNING = 24 # Variable c_int '24'
CODEC_FLAG_LOW_DELAY = 524288 # Variable c_int '524288'
AVSEEK_FLAG_BACKWARD = 1 # Variable c_int '1'
AV_LOG_VERBOSE = 40 # Variable c_int '40'
__mbstate_t_defined = 1 # Variable c_int '1'
FF_PROFILE_MPEG4_SIMPLE = 0 # Variable c_int '0'
M_LOG10E = 0.4342944819032518 # Variable c_double '4.3429448190325181666793241674895398318767547607421875e-1'
MB_TYPE_16x8 = 16 # Variable c_int '16'
CLOCK_MONOTONIC_COARSE = 6 # Variable c_int '6'
__time_t_defined = 1 # Variable c_int '1'
EMSGSIZE = 90 # Variable c_int '90'
AV_PERM_READ = 1 # Variable c_int '1'
AV_CH_BACK_CENTER = 256 # Variable c_int '256'
M_PI = 3.141592653589793 # Variable c_double '3.141592653589793115997963468544185161590576171875e+0'
EL3RST = 47 # Variable c_int '47'
EREMOTEIO = 121 # Variable c_int '121'
PARSER_FLAG_USE_CODEC_TS = 4096 # Variable c_int '4096'
_POSIX_SOURCE = 1 # Variable c_int '1'
CODEC_CAP_VARIABLE_FRAME_SIZE = 65536 # Variable c_int '65536'
SWS_CS_DEFAULT = 5 # Variable c_int '5'
_BITS_TYPESIZES_H = 1 # Variable c_int '1'
LIBSWSCALE_VERSION_MICRO = 100 # Variable c_int '100'
M_PI_2 = 1.5707963267948966 # Variable c_double '1.5707963267948965579989817342720925807952880859375e+0'
FF_PROFILE_DTS_HD_MA = 60 # Variable c_int '60'
M_PI_4 = 0.7853981633974483 # Variable c_double '7.8539816339744827899949086713604629039764404296875e-1'
_ALLOCA_H = 1 # Variable c_int '1'
AV_CH_TOP_CENTER = 2048 # Variable c_int '2048'
SWS_CS_SMPTE240M = 7 # Variable c_int '7'
FF_DTG_AFD_SAME = 8 # Variable c_int '8'
ELNRNG = 48 # Variable c_int '48'
AV_CH_LAYOUT_NATIVE = 9223372036854775808L # Variable c_ulonglong '-9223372036854775808ull'
SWS_BILINEAR = 2 # Variable c_int '2'
____gwchar_t_defined = 1 # Variable c_int '1'
ERESTART = 85 # Variable c_int '85'
__USE_POSIX199309 = 1 # Variable c_int '1'
AVFMT_GLOBALHEADER = 64 # Variable c_int '64'
FF_CMP_CHROMA = 256 # Variable c_int '256'
AV_LOG_FATAL = 8 # Variable c_int '8'
FF_MB_DECISION_RD = 2 # Variable c_int '2'
ENOANO = 55 # Variable c_int '55'
FF_IDCT_SIMPLEARM = 10 # Variable c_int '10'
FF_BUG_QPEL_CHROMA = 64 # Variable c_int '64'
EUCLEAN = 117 # Variable c_int '117'
ENOPROTOOPT = 92 # Variable c_int '92'
FF_PROFILE_H264_CONSTRAINED = 512 # Variable c_int '512'
AV_CH_TOP_FRONT_CENTER = 8192 # Variable c_int '8192'
NGROUPS_MAX = 65536 # Variable c_int '65536'
FF_BUFFER_TYPE_SHARED = 4 # Variable c_int '4'
FF_BUFFER_HINTS_REUSABLE = 8 # Variable c_int '8'
_G_HAVE_MMAP = 1 # Variable c_int '1'
WORD_BIT = 32 # Variable c_int '32'
AV_CH_WIDE_LEFT = 2147483648L # Variable c_ulonglong '2147483648ull'
AVERROR_INVALIDDATA = -1094995529 # Variable c_int '-0x00000000041444e49'
FF_DTG_AFD_16_9_SP_14_9 = 14 # Variable c_int '14'
MB_LEN_MAX = 16 # Variable c_int '16'
WUNTRACED = 2 # Variable c_int '2'
AV_LOG_QUIET = -8 # Variable c_int '-0x00000000000000008'
__SIZEOF_PTHREAD_BARRIER_T = 32 # Variable c_int '32'
FF_CODER_TYPE_RLE = 3 # Variable c_int '3'
AV_CH_LAYOUT_QUAD = 51 # Variable c_int '51'
FF_DEBUG_VIS_QP = 8192 # Variable c_int '8192'
AV_CPU_FLAG_SSSE3 = 128 # Variable c_int '128'
_IOS_BIN = 128 # Variable c_int '128'
CLOCK_REALTIME_COARSE = 5 # Variable c_int '5'
CODEC_CAP_NEG_LINESIZES = 2048 # Variable c_int '2048'
_POSIX_THREAD_KEYS_MAX = 128 # Variable c_int '128'
AV_CH_LAYOUT_MONO = 4 # Variable c_int '4'
_IO_SKIPWS = 1 # Variable c_int '1'
ECONNRESET = 104 # Variable c_int '104'
_SYS_TYPES_H = 1 # Variable c_int '1'
FF_PROFILE_MPEG4_SIMPLE_FACE_ANIMATION = 6 # Variable c_int '6'
CODEC_FLAG_QPEL = 16 # Variable c_int '16'
CODEC_CAP_AUTO_THREADS = 32768 # Variable c_int '32768'
FF_DCT_MMX = 3 # Variable c_int '3'
_IOS_ATEND = 4 # Variable c_int '4'
_IO_SCIENTIFIC = 2048 # Variable c_int '2048'
CLOCK_THREAD_CPUTIME_ID = 3 # Variable c_int '3'
EL3HLT = 46 # Variable c_int '46'
M_LN10 = 2.302585092994046 # Variable c_double '2.30258509299404590109361379290930926799774169921875e+0'
AV_EF_EXPLODE = 8 # Variable c_int '8'
CODEC_FLAG_EMU_EDGE = 16384 # Variable c_int '16384'
E2BIG = 7 # Variable c_int '7'
AV_PERM_NEG_LINESIZES = 32 # Variable c_int '32'
FF_PROFILE_H264_CONSTRAINED_BASELINE = 578 # Variable c_int '578'
FF_PROFILE_MPEG4_MAIN = 3 # Variable c_int '3'
EPIPE = 32 # Variable c_int '32'
FF_LOSS_COLORQUANT = 16 # Variable c_int '16'
ERFKILL = 132 # Variable c_int '132'
EHOSTDOWN = 112 # Variable c_int '112'
EINTR = 4 # Variable c_int '4'
EBFONT = 59 # Variable c_int '59'
EXFULL = 54 # Variable c_int '54'
FF_DCT_FAAN = 6 # Variable c_int '6'
AV_DISPOSITION_LYRICS = 16 # Variable c_int '16'
FF_LAMBDA_MAX = 32767 # Variable c_int '32767'
SWS_BICUBIC = 4 # Variable c_int '4'
EBUSY = 16 # Variable c_int '16'
AVFMT_ALLOW_FLUSH = 65536 # Variable c_int '65536'
FF_BUFFER_TYPE_INTERNAL = 1 # Variable c_int '1'
FF_PROFILE_H264_HIGH = 100 # Variable c_int '100'
_POSIX_STREAM_MAX = 8 # Variable c_int '8'
FF_PROFILE_H264_INTRA = 2048 # Variable c_int '2048'
EADDRINUSE = 98 # Variable c_int '98'
AVIO_SEEKABLE_NORMAL = 1 # Variable c_int '1'
_IO_ERR_SEEN = 32 # Variable c_int '32'
FF_IDCT_SIMPLENEON = 22 # Variable c_int '22'
AV_PARSER_PTS_NB = 4 # Variable c_int '4'
RTSIG_MAX = 32 # Variable c_int '32'
FF_DEBUG_BITSTREAM = 4 # Variable c_int '4'
FF_COMPLIANCE_EXPERIMENTAL = -2 # Variable c_int '-0x00000000000000002'
_IOS_TRUNC = 16 # Variable c_int '16'
AV_PKT_FLAG_KEY = 1 # Variable c_int '1'
AV_DICT_DONT_OVERWRITE = 16 # Variable c_int '16'
AV_DICT_MATCH_CASE = 1 # Variable c_int '1'
FF_BUG_NO_PADDING = 16 # Variable c_int '16'
AV_DISPOSITION_KARAOKE = 32 # Variable c_int '32'
_POSIX_MAX_INPUT = 255 # Variable c_int '255'
FF_DTG_AFD_4_3_SP_14_9 = 13 # Variable c_int '13'
_ENDIAN_H = 1 # Variable c_int '1'
ELIBACC = 79 # Variable c_int '79'
LIBAVDEVICE_VERSION_MAJOR = 54 # Variable c_int '54'
__USE_FORTIFY_LEVEL = 2 # Variable c_int '2'
FF_BUG_OLD_MSMPEG4 = 2 # Variable c_int '2'
CODEC_FLAG_INTERLACED_ME = 536870912 # Variable c_int '536870912'
AV_CH_LAYOUT_7POINT1_WIDE = 1743 # Variable c_int '1743'
LIBPOSTPROC_VERSION_MINOR = 0 # Variable c_int '0'
EDQUOT = 122 # Variable c_int '122'
AVFILTER_CMD_FLAG_ONE = 1 # Variable c_int '1'
ENOENT = 2 # Variable c_int '2'
__SIZEOF_PTHREAD_CONDATTR_T = 4 # Variable c_int '4'
FF_QSCALE_TYPE_H264 = 2 # Variable c_int '2'
MAX_REORDER_DELAY = 16 # Variable c_int '16'
MB_TYPE_8x16 = 32 # Variable c_int '32'
WCONTINUED = 8 # Variable c_int '8'
__USE_XOPEN_EXTENDED = 1 # Variable c_int '1'
_POSIX_HOST_NAME_MAX = 255 # Variable c_int '255'
SEEK_END = 2 # Variable c_int '2'
FF_PROFILE_MPEG4_BASIC_ANIMATED_TEXTURE = 7 # Variable c_int '7'
AV_PERM_REUSE = 8 # Variable c_int '8'
M_PHI = 1.618033988749895 # Variable c_double '1.6180339887498949025257388711906969547271728515625e+0'
FF_PROFILE_RESERVED = -100 # Variable c_int '-0x00000000000000064'
SWS_CS_FCC = 4 # Variable c_int '4'
AV_CH_LOW_FREQUENCY = 8 # Variable c_int '8'
FF_PROFILE_MPEG4_ADVANCED_CODING = 11 # Variable c_int '11'
SWS_DIRECT_BGR = 32768 # Variable c_int '32768'
AV_CH_LAYOUT_5POINT0_BACK = 55 # Variable c_int '55'
AVFMT_VARIABLE_FPS = 1024 # Variable c_int '1024'
HUGE_VAL = 0.0 # Variable c_double '0.0'
_POSIX_NGROUPS_MAX = 8 # Variable c_int '8'
_IO_BOOLALPHA = 65536 # Variable c_int '65536'
CODEC_FLAG2_FAST = 1 # Variable c_int '1'
ENOTEMPTY = 39 # Variable c_int '39'
FF_MIN_BUFFER_SIZE = 16384 # Variable c_int '16384'
_IO_UNITBUF = 8192 # Variable c_int '8192'
__USE_BSD = 1 # Variable c_int '1'
ENOTDIR = 20 # Variable c_int '20'
M_1_PI = 0.3183098861837907 # Variable c_double '3.18309886183790691216444201927515678107738494873046875e-1'
SWS_SINC = 256 # Variable c_int '256'
SWS_CPU_CAPS_3DNOW = 1073741824 # Variable c_int '1073741824'
UNDERFLOW = 4 # Variable c_int '4'
PIPE_BUF = 4096 # Variable c_int '4096'
__SIZEOF_PTHREAD_MUTEX_T = 40 # Variable c_int '40'
FF_CMP_W53 = 11 # Variable c_int '11'
FF_CMP_SAD = 0 # Variable c_int '0'
AVIO_FLAG_READ = 1 # Variable c_int '1'
LIBSWSCALE_VERSION_MAJOR = 2 # Variable c_int '2'
AVFMT_FLAG_CUSTOM_IO = 128 # Variable c_int '128'
FF_PROFILE_MPEG2_MAIN = 4 # Variable c_int '4'
HUGE = 3.4028234663852886e+38 # Variable c_float '3.4028234663852885981170418348451692544e+38f'
FF_THREAD_FRAME = 1 # Variable c_int '1'
M_2_PI = 0.6366197723675814 # Variable c_double '6.3661977236758138243288840385503135621547698974609375e-1'
EDESTADDRREQ = 89 # Variable c_int '89'
ENETRESET = 102 # Variable c_int '102'
_POSIX_SYMLINK_MAX = 255 # Variable c_int '255'
AV_CPU_FLAG_SSE4 = 256 # Variable c_int '256'
AV_CPU_FLAG_SSE3 = 64 # Variable c_int '64'
AV_CPU_FLAG_SSE2 = 16 # Variable c_int '16'
EAFNOSUPPORT = 97 # Variable c_int '97'
_G_config_h = 1 # Variable c_int '1'
CODEC_FLAG_CLOSED_GOP = 2147483648L # Variable c_uint '2147483648u'
CODEC_CAP_PARAM_CHANGE = 16384 # Variable c_int '16384'
EHOSTUNREACH = 113 # Variable c_int '113'
WEXITED = 4 # Variable c_int '4'
AV_CPU_FLAG_3DNOW = 4 # Variable c_int '4'
_XOPEN_SOURCE = 700 # Variable c_int '700'
__USE_EXTERN_INLINES_IN_LIBC = 1 # Variable c_int '1'
__USE_ISOC95 = 1 # Variable c_int '1'
FF_FDEBUG_TS = 1 # Variable c_int '1'
CODEC_FLAG_GLOBAL_HEADER = 4194304 # Variable c_int '4194304'
FF_CMP_RD = 6 # Variable c_int '6'
FF_DCT_AUTO = 0 # Variable c_int '0'
__GLIBC__ = 2 # Variable c_int '2'
__USE_ISOC99 = 1 # Variable c_int '1'
CODEC_FLAG2_SKIP_RD = 16384 # Variable c_int '16384'
AV_CH_LAYOUT_STEREO_DOWNMIX = 1610612736 # Variable c_int '1610612736'
AV_PROGRAM_RUNNING = 1 # Variable c_int '1'
EMEDIUMTYPE = 124 # Variable c_int '124'
_IO_SHOWBASE = 128 # Variable c_int '128'
LIBSWSCALE_IDENT = 'SwS2.1.100' # Variable STRING '(const char*)"SwS2.1.100"'
FF_COMPLIANCE_VERY_STRICT = 2 # Variable c_int '2'
FF_IDCT_LIBMPEG2MMX = 4 # Variable c_int '4'
AV_NOPTS_VALUE = 9223372036854775808L # Variable c_ulong '-9223372036854775808ul'
FF_LOSS_RESOLUTION = 1 # Variable c_int '1'
FF_QSCALE_TYPE_VP56 = 3 # Variable c_int '3'
_IOS_NOREPLACE = 64 # Variable c_int '64'
CODEC_CAP_DRAW_HORIZ_BAND = 1 # Variable c_int '1'
_XLOCALE_H = 1 # Variable c_int '1'
FF_DEBUG_PTS = 512 # Variable c_int '512'
ENODEV = 19 # Variable c_int '19'
ENOCSI = 50 # Variable c_int '50'
FF_COMPLIANCE_UNOFFICIAL = -1 # Variable c_int '-0x00000000000000001'
EPROTONOSUPPORT = 93 # Variable c_int '93'
_G_HAVE_IO_GETLINE_INFO = 1 # Variable c_int '1'
__STDLIB_MB_LEN_MAX = 16 # Variable c_int '16'
FF_PROFILE_MPEG4_SCALABLE_TEXTURE = 5 # Variable c_int '5'
_SVID_SOURCE = 1 # Variable c_int '1'
ETIME = 62 # Variable c_int '62'
__WCLONE = 2147483648L # Variable c_uint '2147483648u'
_INTTYPES_H = 1 # Variable c_int '1'
AV_CH_SIDE_LEFT = 512 # Variable c_int '512'
_IONBF = 2 # Variable c_int '2'
__USE_XOPEN = 1 # Variable c_int '1'
__error_t_defined = 1 # Variable c_int '1'
SWS_CPU_CAPS_SSE2 = 33554432 # Variable c_int '33554432'
XATTR_SIZE_MAX = 65536 # Variable c_int '65536'
FF_IDCT_SIMPLEMMX = 3 # Variable c_int '3'
AV_DISPOSITION_DEFAULT = 1 # Variable c_int '1'
MAX_INPUT = 255 # Variable c_int '255'
FF_BUG_DIRECT_BLOCKSIZE = 512 # Variable c_int '512'
CODEC_FLAG_4MV = 4 # Variable c_int '4'
__USE_POSIX2 = 1 # Variable c_int '1'
ELIBEXEC = 83 # Variable c_int '83'
EMLINK = 31 # Variable c_int '31'
AVFMT_NOTIMESTAMPS = 128 # Variable c_int '128'
FF_PROFILE_MPEG2_SIMPLE = 5 # Variable c_int '5'
MB_TYPE_INTRA4x4 = 1 # Variable c_int '1'
FF_IDCT_VP3 = 12 # Variable c_int '12'
FF_IDCT_SIMPLEARMV6 = 17 # Variable c_int '17'
FF_CMP_DCT264 = 14 # Variable c_int '14'
SWS_ACCURATE_RND = 262144 # Variable c_int '262144'
LIBAVFORMAT_VERSION_MICRO = 100 # Variable c_int '100'
_G_HAVE_LONG_DOUBLE_IO = 1 # Variable c_int '1'
FF_EC_GUESS_MVS = 1 # Variable c_int '1'
_POSIX_MAX_CANON = 255 # Variable c_int '255'
AIO_PRIO_DELTA_MAX = 20 # Variable c_int '20'
_IO_RIGHT = 4 # Variable c_int '4'
_IOS_APPEND = 8 # Variable c_int '8'
AV_CH_LAYOUT_7POINT1_WIDE_BACK = 255 # Variable c_int '255'
PARSER_FLAG_ONCE = 2 # Variable c_int '2'
FF_DTG_AFD_16_9 = 10 # Variable c_int '10'
AVFMT_FLAG_IGNIDX = 2 # Variable c_int '2'
FF_PRED_MEDIAN = 2 # Variable c_int '2'
_POSIX_THREAD_THREADS_MAX = 64 # Variable c_int '64'
_LIBC_LIMITS_H_ = 1 # Variable c_int '1'
__USE_ATFILE = 1 # Variable c_int '1'
SWS_LANCZOS = 512 # Variable c_int '512'
AV_EF_CAREFUL = 65536 # Variable c_int '65536'
AVFMT_NODIMENSIONS = 2048 # Variable c_int '2048'
PP_FORMAT_420 = 25 # Variable c_int '25'
FF_CMP_SSE = 1 # Variable c_int '1'
PP_FORMAT_422 = 9 # Variable c_int '9'
LIBAVUTIL_VERSION_MAJOR = 51 # Variable c_int '51'
AVERROR_EXIT = -1414092869 # Variable c_int '-0x00000000054495845'
_POSIX2_CHARCLASS_NAME_MAX = 14 # Variable c_int '14'
AV_LOG_DEBUG = 48 # Variable c_int '48'
__USE_POSIX = 1 # Variable c_int '1'
DELAYTIMER_MAX = 2147483647 # Variable c_int '2147483647'
FF_DEBUG_MMCO = 2048 # Variable c_int '2048'
_IO_NO_WRITES = 8 # Variable c_int '8'
SLICE_FLAG_CODED_ORDER = 1 # Variable c_int '1'
TMP_MAX = 238328 # Variable c_int '238328'
FF_CMP_W97 = 12 # Variable c_int '12'
_G_HAVE_IO_FILE_OPEN = 1 # Variable c_int '1'
__WORDSIZE = 64 # Variable c_int '64'
FF_BUFFER_TYPE_USER = 2 # Variable c_int '2'
PTHREAD_STACK_MIN = 16384 # Variable c_int '16384'
FF_PRED_LEFT = 0 # Variable c_int '0'
AVFMT_FLAG_NONBLOCK = 4 # Variable c_int '4'
SWS_CS_ITU624 = 5 # Variable c_int '5'
FF_DEBUG_MB_TYPE = 8 # Variable c_int '8'
FF_INPUT_BUFFER_PADDING_SIZE = 16 # Variable c_int '16'
UCHAR_MAX = 255 # Variable c_int '255'
SWS_CPU_CAPS_MMX2 = 536870912 # Variable c_int '536870912'
_IO_NO_READS = 4 # Variable c_int '4'
CODEC_FLAG_QP_RD = 134217728 # Variable c_int '134217728'
EISCONN = 106 # Variable c_int '106'
_IO_MAGIC_MASK = 4294901760L # Variable c_uint '4294901760u'
_BITS_WCHAR_H = 1 # Variable c_int '1'
__GLIBC_MINOR__ = 13 # Variable c_int '13'
FF_PROFILE_DTS_96_24 = 40 # Variable c_int '40'
AV_TIME_BASE = 1000000 # Variable c_int '1000000'
PP_FORMAT = 8 # Variable c_int '8'
PP_CPU_CAPS_MMX = 2147483648L # Variable c_uint '2147483648u'
CODEC_FLAG_QSCALE = 2 # Variable c_int '2'
FF_BUFFER_TYPE_COPY = 8 # Variable c_int '8'
_POSIX_CLOCKRES_MIN = 20000000 # Variable c_int '20000000'
LIBAVUTIL_VERSION_MINOR = 60 # Variable c_int '60'
FF_DEBUG_BUGS = 4096 # Variable c_int '4096'
AVFMT_NOSTREAMS = 4096 # Variable c_int '4096'
_IO_IS_APPENDING = 4096 # Variable c_int '4096'
FF_DTG_AFD_SP_4_3 = 15 # Variable c_int '15'
FF_PROFILE_MPEG4_CORE = 2 # Variable c_int '2'
AVPROBE_SCORE_MAX = 100 # Variable c_int '100'
ELOOP = 40 # Variable c_int '40'
FF_PROFILE_MPEG4_ADVANCED_CORE = 12 # Variable c_int '12'
EREMOTE = 66 # Variable c_int '66'
FF_CMP_NSSE = 10 # Variable c_int '10'
FF_PROFILE_H264_EXTENDED = 88 # Variable c_int '88'
CODEC_CAP_CHANNEL_CONF = 1024 # Variable c_int '1024'
FF_DEBUG_THREADS = 65536 # Variable c_int '65536'
FF_IDCT_SIMPLE = 2 # Variable c_int '2'
FF_LEVEL_UNKNOWN = -99 # Variable c_int '-0x00000000000000063'
FF_PROFILE_DTS = 20 # Variable c_int '20'
_G_VTABLE_LABEL_HAS_LENGTH = 1 # Variable c_int '1'
_BITS_POSIX2_LIM_H = 1 # Variable c_int '1'
MB_TYPE_INTERLACED = 128 # Variable c_int '128'
AV_CPU_FLAG_ATOM = 268435456 # Variable c_int '268435456'
AV_CPU_FLAG_MMX2 = 2 # Variable c_int '2'
FF_LOSS_COLORSPACE = 4 # Variable c_int '4'
__USE_GNU = 1 # Variable c_int '1'
AV_CH_LAYOUT_STEREO = 3 # Variable c_int '3'
_POSIX_MQ_PRIO_MAX = 32 # Variable c_int '32'
SWS_CS_ITU601 = 5 # Variable c_int '5'
SLICE_FLAG_ALLOW_FIELD = 2 # Variable c_int '2'
AVERROR_PROTOCOL_NOT_FOUND = -1330794744 # Variable c_int '-0x0000000004f5250f8'
AV_CPU_FLAG_ARMV5TE = 1 # Variable c_int '1'
_G_IO_IO_FILE_VERSION = 131073 # Variable c_int '131073'
ELIBMAX = 82 # Variable c_int '82'
_POSIX_C_SOURCE = 200809 # Variable c_long '200809l'
EMULTIHOP = 72 # Variable c_int '72'
AVFMT_RAWPICTURE = 32 # Variable c_int '32'
AV_CH_LAYOUT_5POINT1_BACK = 63 # Variable c_int '63'
AV_CH_LAYOUT_2POINT1 = 11 # Variable c_int '11'
AV_HAVE_FAST_UNALIGNED = 1 # Variable c_int '1'
CODEC_FLAG_PSNR = 32768 # Variable c_int '32768'
AVERROR_MUXER_NOT_FOUND = -1481985528 # Variable c_int '-0x00000000058554df8'
PLOSS = 6 # Variable c_int '6'
_POSIX2_COLL_WEIGHTS_MAX = 2 # Variable c_int '2'
__SIZEOF_PTHREAD_MUTEXATTR_T = 4 # Variable c_int '4'
__USE_SVID = 1 # Variable c_int '1'
AV_CH_LAYOUT_7POINT0_FRONT = 1735 # Variable c_int '1735'
__USE_ANSI = 1 # Variable c_int '1'
AV_CH_LAYOUT_7POINT0 = 1591 # Variable c_int '1591'
_IO_OCT = 32 # Variable c_int '32'
FF_PROFILE_MPEG4_ADVANCED_SIMPLE = 15 # Variable c_int '15'
CHARCLASS_NAME_MAX = 2048 # Variable c_int '2048'
__ldiv_t_defined = 1 # Variable c_int '1'
FP_ILOGB0 = -2147483648 # Variable c_int '-0x00000000080000000'
LIBPOSTPROC_VERSION_MAJOR = 52 # Variable c_int '52'
FF_IDCT_FAAN = 20 # Variable c_int '20'
LIBAVFILTER_VERSION_MICRO = 100 # Variable c_int '100'
M_LOG2E = 1.4426950408889634 # Variable c_double '1.442695040888963387004650940070860087871551513671875e+0'
ENOTUNIQ = 76 # Variable c_int '76'
FF_IDCT_INT = 1 # Variable c_int '1'
__timer_t_defined = 1 # Variable c_int '1'
ECONNABORTED = 103 # Variable c_int '103'
EISNAM = 120 # Variable c_int '120'
L_ctermid = 9 # Variable c_int '9'
FF_BUG_UMP4 = 8 # Variable c_int '8'
AVFMT_FLAG_PRIV_OPT = 131072 # Variable c_int '131072'
FF_IDCT_SIMPLEVIS = 18 # Variable c_int '18'
AV_PERM_ALIGN = 64 # Variable c_int '64'
_POSIX_PATH_MAX = 256 # Variable c_int '256'
ENOKEY = 126 # Variable c_int '126'
_IO_INTERNAL = 8 # Variable c_int '8'
__SIZEOF_PTHREAD_RWLOCK_T = 56 # Variable c_int '56'
MB_TYPE_DIRECT2 = 256 # Variable c_int '256'
FF_IDCT_XVIDMMX = 14 # Variable c_int '14'
__STDC_ISO_10646__ = 200009 # Variable c_long '200009l'
_IOS_NOCREATE = 32 # Variable c_int '32'
SWS_SRC_V_CHR_DROP_MASK = 196608 # Variable c_int '196608'
SWS_PRINT_INFO = 4096 # Variable c_int '4096'
_IO_TIED_PUT_GET = 1024 # Variable c_int '1024'
FF_DCT_INT = 2 # Variable c_int '2'
FF_DEBUG_QP = 16 # Variable c_int '16'
MB_TYPE_ACPRED = 512 # Variable c_int '512'
FF_PROFILE_MPEG2_HIGH = 1 # Variable c_int '1'
__USE_LARGEFILE = 1 # Variable c_int '1'
__USE_EXTERN_INLINES = 1 # Variable c_int '1'
MB_TYPE_L1 = 49152 # Variable c_int '49152'
SWS_MAX_REDUCE_CUTOFF = 0.002 # Variable c_double '2.00000000000000004163336342344337026588618755340576171875e-3'
AV_CH_TOP_FRONT_RIGHT = 16384 # Variable c_int '16384'
_FEATURES_H = 1 # Variable c_int '1'
ULONG_MAX = 18446744073709551615L # Variable c_ulong '-1ul'
FF_COMPLIANCE_STRICT = 1 # Variable c_int '1'
FF_PROFILE_MPEG2_SNR_SCALABLE = 3 # Variable c_int '3'
_G_HAVE_BOOL = 1 # Variable c_int '1'
_LARGEFILE_SOURCE = 1 # Variable c_int '1'
_IOS_INPUT = 1 # Variable c_int '1'
MB_TYPE_16x16 = 8 # Variable c_int '8'
EDOM = 33 # Variable c_int '33'
_POSIX_SEM_NSEMS_MAX = 256 # Variable c_int '256'
AV_CPU_FLAG_ALTIVEC = 1 # Variable c_int '1'
_BITS_TYPES_H = 1 # Variable c_int '1'
AV_CPU_FLAG_SSE42 = 512 # Variable c_int '512'
AVFMT_NOFILE = 1 # Variable c_int '1'
AV_PERM_PRESERVE = 4 # Variable c_int '4'
EILSEQ = 84 # Variable c_int '84'
CODEC_FLAG2_CHUNKS = 32768 # Variable c_int '32768'
FF_PROFILE_UNKNOWN = -99 # Variable c_int '-0x00000000000000063'
TIMER_ABSTIME = 1 # Variable c_int '1'
AVFMT_TS_NONSTRICT = 134348800 # Variable c_int '134348800'
AVFMT_NEEDNUMBER = 2 # Variable c_int '2'
AVFMT_NO_BYTE_SEEK = 32768 # Variable c_int '32768'
SING = 2 # Variable c_int '2'
EPFNOSUPPORT = 96 # Variable c_int '96'
FF_PROFILE_H264_HIGH_422 = 122 # Variable c_int '122'
EFAULT = 14 # Variable c_int '14'
SLICE_FLAG_ALLOW_PLANE = 4 # Variable c_int '4'
AV_DISPOSITION_FORCED = 64 # Variable c_int '64'
ENONET = 64 # Variable c_int '64'
ECHRNG = 44 # Variable c_int '44'
FF_BUFFER_HINTS_READABLE = 2 # Variable c_int '2'
_XOPEN_SOURCE_EXTENDED = 1 # Variable c_int '1'
PP_FORMAT_411 = 10 # Variable c_int '10'
FF_BUG_HPEL_CHROMA = 2048 # Variable c_int '2048'
AV_EF_COMPLIANT = 131072 # Variable c_int '131072'
CLOCKS_PER_SEC = 1000000 # Variable c_long '1000000l'
WNOWAIT = 16777216 # Variable c_int '16777216'
FF_PROFILE_MPEG2_422 = 0 # Variable c_int '0'
AVIO_FLAG_WRITE = 2 # Variable c_int '2'
AV_PERM_WRITE = 2 # Variable c_int '2'
_IO_UNBUFFERED = 2 # Variable c_int '2'
AVFMT_GENERIC_INDEX = 256 # Variable c_int '256'
ESRCH = 3 # Variable c_int '3'
FF_DEBUG_BUFFERS = 32768 # Variable c_int '32768'
RE_DUP_MAX = 32767 # Variable c_int '32767'
FF_DEBUG_VIS_MV_B_FOR = 2 # Variable c_int '2'
FF_CMP_VSSE = 9 # Variable c_int '9'
FF_PROFILE_H264_MAIN = 77 # Variable c_int '77'
SWS_CPU_CAPS_MMX = 2147483648L # Variable c_uint '2147483648u'
AVFMT_FLAG_MP4A_LATM = 32768 # Variable c_int '32768'
SWS_FAST_BILINEAR = 1 # Variable c_int '1'
AV_PERM_REUSE2 = 16 # Variable c_int '16'
EHWPOISON = 133 # Variable c_int '133'
XATTR_NAME_MAX = 255 # Variable c_int '255'
LOGIN_NAME_MAX = 256 # Variable c_int '256'
FF_CMP_DCT = 3 # Variable c_int '3'
HUGE_VALF = 0.0 # Variable c_float '0.0f'
FF_DEBUG_VIS_MV_B_BACK = 4 # Variable c_int '4'
AV_CPU_FLAG_ARMV6T2 = 4 # Variable c_int '4'
_POSIX_AIO_MAX = 1 # Variable c_int '1'
AV_LOG_INFO = 32 # Variable c_int '32'
AV_NUM_DATA_POINTERS = 8 # Variable c_int '8'
PATH_MAX = 4096 # Variable c_int '4096'
EL2NSYNC = 45 # Variable c_int '45'
AV_LOG_MAX_OFFSET = 56 # Variable c_int '56'
AV_CPU_FLAG_VFPV3 = 16 # Variable c_int '16'
AV_CH_BACK_RIGHT = 32 # Variable c_int '32'
ENOMSG = 42 # Variable c_int '42'
FF_DEBUG_VIS_MB_TYPE = 16384 # Variable c_int '16384'
MB_TYPE_INTRA16x16 = 2 # Variable c_int '2'
LIBAVDEVICE_VERSION_MINOR = 0 # Variable c_int '0'
__FD_ZERO_STOS = 'stosq' # Variable STRING '(const char*)"stosq"'
EISDIR = 21 # Variable c_int '21'
AVFMTCTX_NOHEADER = 1 # Variable c_int '1'
LIBAVFILTER_VERSION_MINOR = 82 # Variable c_int '82'
_G_HAVE_SYS_CDEFS = 1 # Variable c_int '1'
FF_CMP_PSNR = 4 # Variable c_int '4'
AV_CH_FRONT_LEFT_OF_CENTER = 64 # Variable c_int '64'
FF_CMP_VSAD = 8 # Variable c_int '8'
FF_BUG_AMV = 32 # Variable c_int '32'
__GNU_LIBRARY__ = 6 # Variable c_int '6'
AV_DISPOSITION_VISUAL_IMPAIRED = 256 # Variable c_int '256'
M_E = 2.718281828459045 # Variable c_double '2.718281828459045090795598298427648842334747314453125e+0'
CODEC_CAP_SMALL_LAST_FRAME = 64 # Variable c_int '64'
FF_MB_DECISION_SIMPLE = 0 # Variable c_int '0'
_IO_USER_BUF = 1 # Variable c_int '1'
__USE_LARGEFILE64 = 1 # Variable c_int '1'
_POSIX_LINK_MAX = 8 # Variable c_int '8'
FF_PROFILE_MPEG2_SS = 2 # Variable c_int '2'
AV_CH_FRONT_RIGHT_OF_CENTER = 128 # Variable c_int '128'
_POSIX_SSIZE_MAX = 32767 # Variable c_int '32767'
LIBAVFORMAT_VERSION_MINOR = 11 # Variable c_int '11'
AV_CH_LAYOUT_4POINT1 = 271 # Variable c_int '271'
ESTRPIPE = 86 # Variable c_int '86'
__STDC_IEC_559_COMPLEX__ = 1 # Variable c_int '1'
EINVAL = 22 # Variable c_int '22'
_IO_LINE_BUF = 512 # Variable c_int '512'
CODEC_CAP_HWACCEL = 16 # Variable c_int '16'
AV_CH_BACK_LEFT = 16 # Variable c_int '16'
ESPIPE = 29 # Variable c_int '29'
AV_CPU_FLAG_SSE2SLOW = 1073741824 # Variable c_int '1073741824'
FF_IDCT_ALTIVEC = 8 # Variable c_int '8'
CODEC_CAP_SUBFRAMES = 256 # Variable c_int '256'
FF_PROFILE_DTS_ES = 30 # Variable c_int '30'
_POSIX_RTSIG_MAX = 8 # Variable c_int '8'
CODEC_FLAG_NORMALIZE_AQP = 131072 # Variable c_int '131072'
_POSIX_SEM_VALUE_MAX = 32767 # Variable c_int '32767'
PP_CPU_CAPS_MMX2 = 536870912 # Variable c_int '536870912'
EBADRQC = 56 # Variable c_int '56'
NAN = 0.0 # Variable c_float '0.0f'
NZERO = 20 # Variable c_int '20'
_IO_LEFT = 2 # Variable c_int '2'
_IO_FLAGS2_MMAP = 1 # Variable c_int '1'
M_LN2 = 0.6931471805599453 # Variable c_double '6.9314718055994528622676398299518041312694549560546875e-1'
_G_USING_THUNKS = 1 # Variable c_int '1'
UINT_MAX = 4294967295L # Variable c_uint '4294967295u'
__GLIBC_HAVE_LONG_LONG = 1 # Variable c_int '1'
CODEC_CAP_TRUNCATED = 8 # Variable c_int '8'
AVFILTER_ALIGN = 16 # Variable c_int '16'
AV_CH_SURROUND_DIRECT_LEFT = 8589934592L # Variable c_ulonglong '8589934592ull'
EOWNERDEAD = 130 # Variable c_int '130'
FOPEN_MAX = 16 # Variable c_int '16'
_IO_DELETE_DONT_CLOSE = 64 # Variable c_int '64'
MB_TYPE_QUANT = 65536 # Variable c_int '65536'
FF_PROFILE_AAC_MAIN = 0 # Variable c_int '0'
CODEC_CAP_LOSSLESS = 2147483648L # Variable c_uint '2147483648u'
FF_PROFILE_MPEG4_SIMPLE_SCALABLE = 1 # Variable c_int '1'
ENOTTY = 25 # Variable c_int '25'
SWS_CPU_CAPS_BFIN = 16777216 # Variable c_int '16777216'
EKEYEXPIRED = 127 # Variable c_int '127'
CODEC_CAP_FRAME_THREADS = 4096 # Variable c_int '4096'
FF_PROFILE_MPEG4_CORE_SCALABLE = 10 # Variable c_int '10'
_STDLIB_H = 1 # Variable c_int '1'
SWS_PARAM_DEFAULT = 123456 # Variable c_int '123456'
__W_CONTINUED = 65535 # Variable c_int '65535'
FF_IDCT_H264 = 11 # Variable c_int '11'
ENOTNAM = 118 # Variable c_int '118'
EUNATCH = 49 # Variable c_int '49'
M_LOG2_10 = 3.321928094887362 # Variable c_double '3.321928094887362181708567732130177319049835205078125e+0'
__SIZEOF_PTHREAD_COND_T = 48 # Variable c_int '48'
_POSIX_TZNAME_MAX = 6 # Variable c_int '6'
CODEC_CAP_DELAY = 32 # Variable c_int '32'
_POSIX_MQ_OPEN_MAX = 8 # Variable c_int '8'
_POSIX_NAME_MAX = 14 # Variable c_int '14'
MB_TYPE_L0 = 12288 # Variable c_int '12288'
AV_CH_LAYOUT_5POINT0 = 1543 # Variable c_int '1543'
AV_CH_LAYOUT_5POINT1 = 1551 # Variable c_int '1551'
__lldiv_t_defined = 1 # Variable c_int '1'
XATTR_LIST_MAX = 65536 # Variable c_int '65536'
__USE_XOPEN2K = 1 # Variable c_int '1'
FF_PROFILE_MPEG4_N_BIT = 4 # Variable c_int '4'
ECHILD = 10 # Variable c_int '10'
FF_DEBUG_ER = 1024 # Variable c_int '1024'
FF_LAMBDA_SHIFT = 7 # Variable c_int '7'
AV_DICT_IGNORE_SUFFIX = 2 # Variable c_int '2'
AV_PKT_FLAG_CORRUPT = 2 # Variable c_int '2'
FF_CMP_SATD = 2 # Variable c_int '2'
FF_COMPRESSION_DEFAULT = -1 # Variable c_int '-0x00000000000000001'
MB_TYPE_8x8 = 64 # Variable c_int '64'
PP_CPU_CAPS_3DNOW = 1073741824 # Variable c_int '1073741824'
SWS_CS_SMPTE170M = 5 # Variable c_int '5'
X_TLOSS = 1.414847550405688e+16 # Variable c_double '1.414847550405688e+16'
FF_DEBUG_PICT_INFO = 1 # Variable c_int '1'
MB_TYPE_P1L0 = 8192 # Variable c_int '8192'
MB_TYPE_P1L1 = 32768 # Variable c_int '32768'
AV_LOG_PANIC = 0 # Variable c_int '0'
_IO_LINKED = 128 # Variable c_int '128'
FF_PROFILE_H264_BASELINE = 66 # Variable c_int '66'
_STRUCT_TIMEVAL = 1 # Variable c_int '1'
EROFS = 30 # Variable c_int '30'
FF_LOSS_ALPHA = 8 # Variable c_int '8'
ENOLINK = 67 # Variable c_int '67'
AV_EF_CRCCHECK = 1 # Variable c_int '1'
FF_PROFILE_H264_HIGH_444_PREDICTIVE = 244 # Variable c_int '244'
EALREADY = 114 # Variable c_int '114'
FF_PROFILE_VC1_ADVANCED = 3 # Variable c_int '3'
__SIZEOF_PTHREAD_BARRIERATTR_T = 4 # Variable c_int '4'
ENXIO = 6 # Variable c_int '6'
EMFILE = 24 # Variable c_int '24'
ECONNREFUSED = 111 # Variable c_int '111'
AV_CH_STEREO_LEFT = 536870912 # Variable c_int '536870912'
L_tmpnam = 20 # Variable c_int '20'
AV_CH_LAYOUT_7POINT1 = 1599 # Variable c_int '1599'
_IO_DONT_CLOSE = 32768 # Variable c_int '32768'
AV_CH_LAYOUT_6POINT1 = 1807 # Variable c_int '1807'
AV_CH_LAYOUT_6POINT0 = 1799 # Variable c_int '1799'
ENFILE = 23 # Variable c_int '23'
EREMCHG = 78 # Variable c_int '78'
CODEC_FLAG_GMC = 32 # Variable c_int '32'
__USE_MISC = 1 # Variable c_int '1'
__BIT_TYPES_DEFINED__ = 1 # Variable c_int '1'
AV_EF_BITSTREAM = 2 # Variable c_int '2'
_POSIX_TTY_NAME_MAX = 9 # Variable c_int '9'
PARSER_FLAG_COMPLETE_FRAMES = 1 # Variable c_int '1'
ENOMEM = 12 # Variable c_int '12'
FP_ILOGBNAN = -2147483648 # Variable c_int '-0x00000000080000000'
FF_IDCT_SIMPLEARMV5TE = 16 # Variable c_int '16'
AV_CPU_FLAG_FMA4 = 2048 # Variable c_int '2048'
ETIMEDOUT = 110 # Variable c_int '110'
M_2_SQRTPI = 1.1283791670955126 # Variable c_double '1.1283791670955125585606992899556644260883331298828125e+0'
ELIBSCN = 81 # Variable c_int '81'
_IO_HEX = 64 # Variable c_int '64'
AV_DICT_DONT_STRDUP_KEY = 4 # Variable c_int '4'
FF_QP2LAMBDA = 118 # Variable c_int '118'
MAX_PROBE_PACKETS = 2500 # Variable c_int '2500'
__PTHREAD_MUTEX_HAVE_PREV = 1 # Variable c_int '1'
_BITS_BYTESWAP_H = 1 # Variable c_int '1'
EBADSLT = 57 # Variable c_int '57'
AVFMT_SEEK_TO_PTS = 67108864 # Variable c_int '67108864'
WNOHANG = 1 # Variable c_int '1'
__WORDSIZE_COMPAT32 = 1 # Variable c_int '1'
FF_DCT_ALTIVEC = 5 # Variable c_int '5'
__timespec_defined = 1 # Variable c_int '1'
FILENAME_MAX = 4096 # Variable c_int '4096'
AV_CH_LAYOUT_6POINT0_FRONT = 1731 # Variable c_int '1731'
_SYS_SYSMACROS_H = 1 # Variable c_int '1'
_POSIX_DELAYTIMER_MAX = 32 # Variable c_int '32'
AV_CPU_FLAG_3DNOWEXT = 32 # Variable c_int '32'
AVIO_FLAG_NONBLOCK = 8 # Variable c_int '8'
EXIT_SUCCESS = 0 # Variable c_int '0'
AVERROR_BUG = -558323010 # Variable c_int '-0x00000000021475542'
LIBAVCODEC_VERSION_MICRO = 100 # Variable c_int '100'
ULLONG_MAX = 18446744073709551615L # Variable c_ulonglong '-1ull'
AVCODEC_MAX_AUDIO_FRAME_SIZE = 192000 # Variable c_int '192000'
AVFMT_SHOW_IDS = 8 # Variable c_int '8'
FF_CODER_TYPE_DEFLATE = 4 # Variable c_int '4'
DOMAIN = 1 # Variable c_int '1'
AV_CH_TOP_BACK_CENTER = 65536 # Variable c_int '65536'
SWS_POINT = 16 # Variable c_int '16'
__USE_POSIX199506 = 1 # Variable c_int '1'
__clockid_t_defined = 1 # Variable c_int '1'
ENOSTR = 60 # Variable c_int '60'
AVFMT_FLAG_SORT_DTS = 65536 # Variable c_int '65536'
_STRING_H = 1 # Variable c_int '1'
FF_BUG_MS = 8192 # Variable c_int '8192'
EACCES = 13 # Variable c_int '13'
_POSIX_SYMLOOP_MAX = 8 # Variable c_int '8'
FF_IDCT_MMI = 5 # Variable c_int '5'
AV_CH_LAYOUT_2_1 = 259 # Variable c_int '259'
AV_CH_SURROUND_DIRECT_RIGHT = 17179869184L # Variable c_ulonglong '17179869184ull'
EIO = 5 # Variable c_int '5'
CODEC_FLAG_PASS2 = 1024 # Variable c_int '1024'
CODEC_FLAG_PASS1 = 512 # Variable c_int '512'
__WCHAR_MIN = -2147483648 # Variable c_int '-0x00000000080000000'
AV_CH_TOP_BACK_LEFT = 32768 # Variable c_int '32768'
FF_DTG_AFD_4_3 = 9 # Variable c_int '9'
FF_IDCT_SIMPLEALPHA = 23 # Variable c_int '23'
FF_CODER_TYPE_AC = 1 # Variable c_int '1'
AVPROBE_PADDING_SIZE = 32 # Variable c_int '32'
__USE_XOPEN2K8XSI = 1 # Variable c_int '1'
AVFMT_NOGENSEARCH = 16384 # Variable c_int '16384'
AVERROR_DEMUXER_NOT_FOUND = -1296385272 # Variable c_int '-0x0000000004d4544f8'
ECANCELED = 125 # Variable c_int '125'
AV_CPU_FLAG_VFP = 8 # Variable c_int '8'
__FILE_defined = 1 # Variable c_int '1'
_SYS_CDEFS_H = 1 # Variable c_int '1'
_OLD_STDIO_MAGIC = 4206624768L # Variable c_uint '4206624768u'
SWS_SRC_V_CHR_DROP_SHIFT = 16 # Variable c_int '16'
FF_DEBUG_VIS_MV_P_FOR = 1 # Variable c_int '1'
_POSIX_AIO_LISTIO_MAX = 2 # Variable c_int '2'
FF_PROFILE_AAC_LTP = 3 # Variable c_int '3'
_IO_IS_FILEBUF = 8192 # Variable c_int '8192'
__SIZEOF_PTHREAD_ATTR_T = 56 # Variable c_int '56'
LONG_BIT = 64 # Variable c_int '64'
_G_HAVE_PRINTF_FP = 1 # Variable c_int '1'
AV_DISPOSITION_DUB = 2 # Variable c_int '2'
SWS_GAUSS = 128 # Variable c_int '128'
CODEC_FLAG_BITEXACT = 8388608 # Variable c_int '8388608'
_POSIX_SIGQUEUE_MAX = 32 # Variable c_int '32'
FF_BUFFER_HINTS_VALID = 1 # Variable c_int '1'
LLONG_MIN = -9223372036854775808 # Variable c_longlong '-0x08000000000000000ll'
ENODATA = 61 # Variable c_int '61'
AV_LOG_ERROR = 16 # Variable c_int '16'
_BITS_TIME_H = 1 # Variable c_int '1'
AV_CH_LAYOUT_4POINT0 = 263 # Variable c_int '263'
CODEC_CAP_EXPERIMENTAL = 512 # Variable c_int '512'
AVERROR_STREAM_NOT_FOUND = -1381258232 # Variable c_int '-0x000000000525453f8'
NAME_MAX = 255 # Variable c_int '255'
CLOCK_PROCESS_CPUTIME_ID = 2 # Variable c_int '2'
AVERROR_BSF_NOT_FOUND = -1179861752 # Variable c_int '-0x000000000465342f8'
CODEC_FLAG2_NO_OUTPUT = 4 # Variable c_int '4'
CODEC_FLAG2_SHOW_ALL = 4194304 # Variable c_int '4194304'
FF_QSCALE_TYPE_MPEG1 = 0 # Variable c_int '0'
FF_IDCT_CAVS = 15 # Variable c_int '15'
FF_QSCALE_TYPE_MPEG2 = 1 # Variable c_int '1'
FF_PROFILE_MPEG4_HYBRID = 8 # Variable c_int '8'
AVERROR_FILTER_NOT_FOUND = -1279870712 # Variable c_int '-0x0000000004c4946f8'
AV_CH_LAYOUT_HEXAGONAL = 311 # Variable c_int '311'
_POSIX2_RE_DUP_MAX = 255 # Variable c_int '255'
SWS_BICUBLIN = 64 # Variable c_int '64'
FF_CMP_DCTMAX = 13 # Variable c_int '13'
WSTOPPED = 2 # Variable c_int '2'
__USE_XOPEN2KXSI = 1 # Variable c_int '1'
_TIME_H = 1 # Variable c_int '1'
AVSEEK_SIZE = 65536 # Variable c_int '65536'
AV_DICT_APPEND = 32 # Variable c_int '32'
ESOCKTNOSUPPORT = 94 # Variable c_int '94'
AVFMT_FLAG_NOFILLIN = 16 # Variable c_int '16'
FF_BUG_STD_QPEL = 128 # Variable c_int '128'
AV_CH_SIDE_RIGHT = 1024 # Variable c_int '1024'
AVERROR_DECODER_NOT_FOUND = -1128613112 # Variable c_int '-0x000000000434544f8'
MB_TYPE_CBP = 131072 # Variable c_int '131072'
FF_DEBUG_STARTCODE = 256 # Variable c_int '256'
CODEC_FLAG_GRAY = 8192 # Variable c_int '8192'
MAX_CANON = 255 # Variable c_int '255'
AVPALETTE_SIZE = 1024 # Variable c_int '1024'
__USE_XOPEN2K8 = 1 # Variable c_int '1'
CODEC_CAP_SLICE_THREADS = 8192 # Variable c_int '8192'
AVIO_FLAG_READ_WRITE = 3 # Variable c_int '3'
FF_MAX_B_FRAMES = 16 # Variable c_int '16'
CLOCK_MONOTONIC_RAW = 4 # Variable c_int '4'
CODEC_FLAG_LOOP_FILTER = 2048 # Variable c_int '2048'
RAND_MAX = 2147483647 # Variable c_int '2147483647'
__SIZEOF_PTHREAD_RWLOCKATTR_T = 8 # Variable c_int '8'
FF_BUG_DC_CLIP = 4096 # Variable c_int '4096'
P_tmpdir = '/tmp' # Variable STRING '(const char*)"/tmp"'
MB_TYPE_GMC = 1024 # Variable c_int '1024'
ENOLCK = 37 # Variable c_int '37'
AVFMT_FLAG_NOPARSE = 32 # Variable c_int '32'
IOV_MAX = 1024 # Variable c_int '1024'
FF_BUG_AC_VLC = 0 # Variable c_int '0'
LIBPOSTPROC_IDENT = 'postproc52.0.100' # Variable STRING '(const char*)"postproc52.0.100"'
SEEK_SET = 0 # Variable c_int '0'
LIBAVCODEC_VERSION_MINOR = 29 # Variable c_int '29'
SHRT_MIN = -32768 # Variable c_int '-0x00000000000008000'
_SYS_SELECT_H = 1 # Variable c_int '1'
_IO_SHOWPOINT = 256 # Variable c_int '256'
FF_PROFILE_DTS_HD_HRA = 50 # Variable c_int '50'
AV_CPU_FLAG_FORCE = 2147483648L # Variable c_uint '2147483648u'
PP_CPU_CAPS_ALTIVEC = 268435456 # Variable c_int '268435456'
FF_BUG_TRUNCATED = 16384 # Variable c_int '16384'
AV_CPU_FLAG_MMX = 1 # Variable c_int '1'
_BITS_PTHREADTYPES_H = 1 # Variable c_int '1'
EBADR = 53 # Variable c_int '53'
CODEC_FLAG_INTERLACED_DCT = 262144 # Variable c_int '262144'
_IO_FLAGS2_NOTCANCEL = 2 # Variable c_int '2'
EEXIST = 17 # Variable c_int '17'
M_SQRT1_2 = 0.7071067811865476 # Variable c_double '7.0710678118654757273731092936941422522068023681640625e-1'
AVSEEK_FLAG_ANY = 4 # Variable c_int '4'
LIBSWSCALE_VERSION_MINOR = 1 # Variable c_int '1'
AVERROR_PATCHWELCOME = -1163346256 # Variable c_int '-0x00000000045574150'
AV_CH_FRONT_RIGHT = 2 # Variable c_int '2'
_G_VTABLE_LABEL_PREFIX = '__vt_' # Variable STRING '(const char*)"__vt_"'
_IOFBF = 0 # Variable c_int '0'
EPROTO = 71 # Variable c_int '71'
FF_DEBUG_RC = 2 # Variable c_int '2'
LIBPOSTPROC_VERSION_MICRO = 100 # Variable c_int '100'
_IO_DEC = 16 # Variable c_int '16'
ESRMNT = 69 # Variable c_int '69'
FF_PROFILE_MPEG4_ADVANCED_REAL_TIME = 9 # Variable c_int '9'
_ISOC95_SOURCE = 1 # Variable c_int '1'
AVFMT_FLAG_DISCARD_CORRUPT = 256 # Variable c_int '256'
FF_PROFILE_AAC_SSR = 2 # Variable c_int '2'
_ISOC99_SOURCE = 1 # Variable c_int '1'
FF_CMP_BIT = 5 # Variable c_int '5'
SWS_CPU_CAPS_ALTIVEC = 268435456 # Variable c_int '268435456'
TLOSS = 5 # Variable c_int '5'
AV_CH_STEREO_RIGHT = 1073741824 # Variable c_int '1073741824'
FF_PROFILE_MPEG4_SIMPLE_STUDIO = 14 # Variable c_int '14'
ULONG_LONG_MAX = 18446744073709551615L # Variable c_ulonglong '-1ull'
AV_CPU_FLAG_AVX = 16384 # Variable c_int '16384'
FF_ASPECT_EXTENDED = 15 # Variable c_int '15'
EXDEV = 18 # Variable c_int '18'
CODEC_CAP_DR1 = 2 # Variable c_int '2'
AV_DISPOSITION_COMMENT = 8 # Variable c_int '8'
AV_CPU_FLAG_SSE3SLOW = 536870912 # Variable c_int '536870912'
_POSIX_TIMER_MAX = 32 # Variable c_int '32'
CODEC_FLAG_INPUT_PRESERVED = 256 # Variable c_int '256'
__clock_t_defined = 1 # Variable c_int '1'
_IO_SHOWPOS = 1024 # Variable c_int '1024'
_STDIO_H = 1 # Variable c_int '1'
_IO_MAGIC = 4222418944L # Variable c_uint '4222418944u'
EBADMSG = 74 # Variable c_int '74'
AV_ERROR_MAX_STRING_SIZE = 64 # Variable c_int '64'
AVFMT_TS_DISCONT = 512 # Variable c_int '512'
AV_HAVE_BIGENDIAN = 0 # Variable c_int '0'
_IO_BAD_SEEN = 16384 # Variable c_int '16384'
ELIBBAD = 80 # Variable c_int '80'
ERANGE = 34 # Variable c_int '34'
_IO_UPPERCASE = 512 # Variable c_int '512'
ESTALE = 116 # Variable c_int '116'
AV_CH_TOP_FRONT_LEFT = 4096 # Variable c_int '4096'
FF_PROFILE_VC1_MAIN = 1 # Variable c_int '1'
AV_DICT_DONT_STRDUP_VAL = 8 # Variable c_int '8'
AV_CH_LAYOUT_6POINT1_FRONT = 1739 # Variable c_int '1739'
FF_IDCT_IPP = 13 # Variable c_int '13'
FF_DEBUG_SKIP = 128 # Variable c_int '128'
_IO_FIXED = 4096 # Variable c_int '4096'
LIBAVFILTER_VERSION_MAJOR = 2 # Variable c_int '2'
AVERROR_ENCODER_NOT_FOUND = -1129203192 # Variable c_int '-0x000000000434e45f8'
EKEYREVOKED = 128 # Variable c_int '128'
CLOCK_MONOTONIC = 1 # Variable c_int '1'
CODEC_FLAG2_LOCAL_HEADER = 8 # Variable c_int '8'
AV_CPU_FLAG_XOP = 1024 # Variable c_int '1024'
ENOTRECOVERABLE = 131 # Variable c_int '131'
ENOBUFS = 105 # Variable c_int '105'
AVFMT_FLAG_IGNDTS = 8 # Variable c_int '8'
_CTYPE_H = 1 # Variable c_int '1'
_BITS_POSIX1_LIM_H = 1 # Variable c_int '1'
AVERROR_UNKNOWN = -1313558101 # Variable c_int '-0x0000000004e4b4e55'
__WNOTHREAD = 536870912 # Variable c_int '536870912'
MATH_ERRNO = 1 # Variable c_int '1'
EADDRNOTAVAIL = 99 # Variable c_int '99'
EADV = 68 # Variable c_int '68'
FF_BUG_XVID_ILACE = 4 # Variable c_int '4'
HOST_NAME_MAX = 64 # Variable c_int '64'
AVFMT_FLAG_GENPTS = 1 # Variable c_int '1'
FF_PROFILE_VC1_SIMPLE = 0 # Variable c_int '0'
ENOSYS = 38 # Variable c_int '38'
SWS_CS_ITU709 = 1 # Variable c_int '1'
PP_FORMAT_444 = 8 # Variable c_int '8'
AV_CH_FRONT_LEFT = 1 # Variable c_int '1'
FF_DEBUG_MV = 32 # Variable c_int '32'
FF_DEBUG_DCT_COEFF = 64 # Variable c_int '64'
MB_TYPE_P0L1 = 16384 # Variable c_int '16384'
FF_EC_DEBLOCK = 2 # Variable c_int '2'
FF_PRED_PLANE = 1 # Variable c_int '1'
FF_PROFILE_H264_HIGH_444_INTRA = 2292 # Variable c_int '2292'
EUSERS = 87 # Variable c_int '87'
CLOCK_REALTIME = 0 # Variable c_int '0'
_IO_IN_BACKUP = 256 # Variable c_int '256'
AV_CH_LAYOUT_2_2 = 1539 # Variable c_int '1539'
_SIGSET_H_types = 1 # Variable c_int '1'
MQ_PRIO_MAX = 32768 # Variable c_int '32768'
____FILE_defined = 1 # Variable c_int '1'
_MATH_H_MATHDEF = 1 # Variable c_int '1'
SEEK_CUR = 1 # Variable c_int '1'
_POSIX_CHILD_MAX = 25 # Variable c_int '25'
AV_CPU_FLAG_CMOV = 16777216 # Variable c_int '16777216'
FF_BUG_EDGE = 1024 # Variable c_int '1024'
_ERRNO_H = 1 # Variable c_int '1'
AV_DISPOSITION_ATTACHED_PIC = 1024 # Variable c_int '1024'
__USE_UNIX98 = 1 # Variable c_int '1'
_IO_STDIO = 16384 # Variable c_int '16384'
OVERFLOW = 3 # Variable c_int '3'
FF_PROFILE_H264_HIGH_444 = 144 # Variable c_int '144'
__STDC_IEC_559__ = 1 # Variable c_int '1'
EPERM = 1 # Variable c_int '1'
FF_PROFILE_VC1_COMPLEX = 2 # Variable c_int '2'
errno = (c_int).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'errno')
_XOPEN_LIM_H = 1 # Variable c_int '1'
RAW_PACKET_BUFFER_SIZE = 2500000 # Variable c_int '2500000'
ENOSR = 63 # Variable c_int '63'
_IOS_OUTPUT = 2 # Variable c_int '2'
AV_CH_LAYOUT_6POINT1_BACK = 319 # Variable c_int '319'
EKEYREJECTED = 129 # Variable c_int '129'
AVSEEK_FORCE = 131072 # Variable c_int '131072'
CODEC_FLAG_MV0 = 64 # Variable c_int '64'
PARSER_FLAG_FETCHED_OFFSET = 4 # Variable c_int '4'
_ATFILE_SOURCE = 1 # Variable c_int '1'
FF_IDCT_ARM = 7 # Variable c_int '7'
SWS_BITEXACT = 524288 # Variable c_int '524288'
CODEC_FLAG_TRUNCATED = 65536 # Variable c_int '65536'
ENOTCONN = 107 # Variable c_int '107'
ENETUNREACH = 101 # Variable c_int '101'
SWS_FULL_CHR_H_INP = 16384 # Variable c_int '16384'
CODEC_FLAG2_STRICT_GOP = 2 # Variable c_int '2'
AVFMT_FLAG_KEEP_SIDE_DATA = 262144 # Variable c_int '262144'
SWS_FULL_CHR_H_INT = 8192 # Variable c_int '8192'
LIBAVCODEC_IDENT = 'Lavc54.29.100' # Variable STRING '(const char*)"Lavc54.29.100"'
FF_BUG_AUTODETECT = 1 # Variable c_int '1'
AV_DISPOSITION_CLEAN_EFFECTS = 512 # Variable c_int '512'
_POSIX_LOGIN_NAME_MAX = 9 # Variable c_int '9'
LIBAVUTIL_VERSION_MICRO = 100 # Variable c_int '100'
SWS_SPLINE = 1024 # Variable c_int '1024'
ESHUTDOWN = 108 # Variable c_int '108'
AVSEEK_FLAG_FRAME = 8 # Variable c_int '8'
ENOSPC = 28 # Variable c_int '28'
PP_QUALITY_MAX = 6 # Variable c_int '6'
FF_IDCT_WMV2 = 19 # Variable c_int '19'
LIBAVFORMAT_IDENT = 'Lavf54.11.100' # Variable STRING '(const char*)"Lavf54.11.100"'
_IO_UNIFIED_JUMPTABLES = 1 # Variable c_int '1'
EL2HLT = 51 # Variable c_int '51'
SEM_VALUE_MAX = 2147483647 # Variable c_int '2147483647'
LIBAVDEVICE_VERSION_MICRO = 100 # Variable c_int '100'
AVERROR_OPTION_NOT_FOUND = -1414549496 # Variable c_int '-0x00000000054504ff8'
FF_PROFILE_H264_HIGH_422_INTRA = 2170 # Variable c_int '2170'
SWS_AREA = 32 # Variable c_int '32'
AV_CH_TOP_BACK_RIGHT = 131072 # Variable c_int '131072'
FF_DTG_AFD_14_9 = 11 # Variable c_int '11'
AV_EF_AGGRESSIVE = 262144 # Variable c_int '262144'
AV_CH_LAYOUT_3POINT1 = 15 # Variable c_int '15'
CODEC_CAP_HWACCEL_VDPAU = 128 # Variable c_int '128'
FF_PROFILE_MPEG4_ADVANCED_SCALABLE_TEXTURE = 13 # Variable c_int '13'
MB_TYPE_L0L1 = 61440 # Variable c_int '61440'
FF_RC_STRATEGY_XVID = 1 # Variable c_int '1'
AVIO_FLAG_DIRECT = 32768 # Variable c_int '32768'
_IO_FLAGS2_USER_WBUF = 8 # Variable c_int '8'
ENETDOWN = 100 # Variable c_int '100'
ENOEXEC = 8 # Variable c_int '8'
FF_LOSS_DEPTH = 2 # Variable c_int '2'
COLL_WEIGHTS_MAX = 255 # Variable c_int '255'
MB_TYPE_SKIP = 2048 # Variable c_int '2048'
AV_EF_BUFFER = 4 # Variable c_int '4'
_POSIX_QLIMIT = 1 # Variable c_int '1'
EBADF = 9 # Variable c_int '9'
EBADE = 52 # Variable c_int '52'
_G_NAMES_HAVE_UNDERSCORE = 0 # Variable c_int '0'
ECOMM = 70 # Variable c_int '70'
CODEC_FLAG_CBP_RD = 67108864 # Variable c_int '67108864'
LIBAVUTIL_IDENT = 'Lavu51.60.100' # Variable STRING '(const char*)"Lavu51.60.100"'
AV_LOG_SKIP_REPEATED = 1 # Variable c_int '1'
EDOTDOT = 73 # Variable c_int '73'
EBADFD = 77 # Variable c_int '77'
_POSIX_RE_DUP_MAX = 255 # Variable c_int '255'
FF_COMPLIANCE_NORMAL = 0 # Variable c_int '0'
AV_CPU_FLAG_NEON = 32 # Variable c_int '32'
AVSEEK_FLAG_BYTE = 2 # Variable c_int '2'
FF_LOSS_CHROMA = 32 # Variable c_int '32'
TTY_NAME_MAX = 32 # Variable c_int '32'
FF_MB_DECISION_BITS = 1 # Variable c_int '1'
AV_DISPOSITION_ORIGINAL = 4 # Variable c_int '4'
AV_CH_FRONT_CENTER = 4 # Variable c_int '4'
_BSD_SOURCE = 1 # Variable c_int '1'
PTHREAD_KEYS_MAX = 1024 # Variable c_int '1024'
ENOMEDIUM = 123 # Variable c_int '123'
_LARGEFILE64_SOURCE = 1 # Variable c_int '1'
EPROTOTYPE = 91 # Variable c_int '91'
ENAVAIL = 119 # Variable c_int '119'
SWS_X = 8 # Variable c_int '8'
__WALL = 1073741824 # Variable c_int '1073741824'
MATH_ERREXCEPT = 2 # Variable c_int '2'
_G_NEED_STDARG_H = 1 # Variable c_int '1'
PP_PICT_TYPE_QP2 = 16 # Variable c_int '16'
_SIGSET_NWORDS = 16L # Variable c_ulong '16ul'
FF_IDCT_AUTO = 0 # Variable c_int '0'
FF_BUG_QPEL_CHROMA2 = 256 # Variable c_int '256'
MB_TYPE_INTRA_PCM = 4 # Variable c_int '4'
FF_PROFILE_H264_HIGH_10_INTRA = 2158 # Variable c_int '2158'
ENOTBLK = 15 # Variable c_int '15'
LONG_LONG_MIN = -9223372036854775808 # Variable c_longlong '-0x08000000000000000ll'
_G_HAVE_ATEXIT = 1 # Variable c_int '1'
FF_CMP_ZERO = 7 # Variable c_int '7'
EIDRM = 43 # Variable c_int '43'
_IO_CURRENTLY_PUTTING = 2048 # Variable c_int '2048'
INT_MIN = -2147483648 # Variable c_int '-0x00000000080000000'
EOVERFLOW = 75 # Variable c_int '75'
EXIT_FAILURE = 1 # Variable c_int '1'
FF_IDCT_SH4 = 9 # Variable c_int '9'
AVINDEX_KEYFRAME = 1 # Variable c_int '1'
M_SQRT2 = 1.4142135623730951 # Variable c_double '1.4142135623730951454746218587388284504413604736328125e+0'
AVERROR_BUG2 = -541545794 # Variable c_int '-0x00000000020475542'
_IOLBF = 1 # Variable c_int '1'
FF_DEFAULT_QUANT_BIAS = 999999 # Variable c_int '999999'
FF_CODER_TYPE_RAW = 2 # Variable c_int '2'
_G_int16_t = c_short
_G_int32_t = c_int
_G_uint16_t = c_ushort
_G_uint32_t = c_uint

# values for unnamed enumeration
__ctype_b_loc = _libraries['/usr/local/lib/libavcodec.so'].__ctype_b_loc
__ctype_b_loc.restype = POINTER(POINTER(c_ushort))
__ctype_b_loc.argtypes = []
__int32_t = c_int
__ctype_tolower_loc = _libraries['/usr/local/lib/libavcodec.so'].__ctype_tolower_loc
__ctype_tolower_loc.restype = POINTER(POINTER(__int32_t))
__ctype_tolower_loc.argtypes = []
__ctype_toupper_loc = _libraries['/usr/local/lib/libavcodec.so'].__ctype_toupper_loc
__ctype_toupper_loc.restype = POINTER(POINTER(__int32_t))
__ctype_toupper_loc.argtypes = []
isalnum = _libraries['/usr/local/lib/libavcodec.so'].isalnum
isalnum.restype = c_int
isalnum.argtypes = [c_int]
isalpha = _libraries['/usr/local/lib/libavcodec.so'].isalpha
isalpha.restype = c_int
isalpha.argtypes = [c_int]
iscntrl = _libraries['/usr/local/lib/libavcodec.so'].iscntrl
iscntrl.restype = c_int
iscntrl.argtypes = [c_int]
isdigit = _libraries['/usr/local/lib/libavcodec.so'].isdigit
isdigit.restype = c_int
isdigit.argtypes = [c_int]
islower = _libraries['/usr/local/lib/libavcodec.so'].islower
islower.restype = c_int
islower.argtypes = [c_int]
isgraph = _libraries['/usr/local/lib/libavcodec.so'].isgraph
isgraph.restype = c_int
isgraph.argtypes = [c_int]
isprint = _libraries['/usr/local/lib/libavcodec.so'].isprint
isprint.restype = c_int
isprint.argtypes = [c_int]
ispunct = _libraries['/usr/local/lib/libavcodec.so'].ispunct
ispunct.restype = c_int
ispunct.argtypes = [c_int]
isspace = _libraries['/usr/local/lib/libavcodec.so'].isspace
isspace.restype = c_int
isspace.argtypes = [c_int]
isupper = _libraries['/usr/local/lib/libavcodec.so'].isupper
isupper.restype = c_int
isupper.argtypes = [c_int]
isxdigit = _libraries['/usr/local/lib/libavcodec.so'].isxdigit
isxdigit.restype = c_int
isxdigit.argtypes = [c_int]
tolower = _libraries['/usr/local/lib/libavcodec.so'].tolower
tolower.restype = c_int
tolower.argtypes = [c_int]
toupper = _libraries['/usr/local/lib/libavcodec.so'].toupper
toupper.restype = c_int
toupper.argtypes = [c_int]
isblank = _libraries['/usr/local/lib/libavcodec.so'].isblank
isblank.restype = c_int
isblank.argtypes = [c_int]
isctype = _libraries['/usr/local/lib/libavcodec.so'].isctype
isctype.restype = c_int
isctype.argtypes = [c_int, c_int]
isascii = _libraries['/usr/local/lib/libavcodec.so'].isascii
isascii.restype = c_int
isascii.argtypes = [c_int]
toascii = _libraries['/usr/local/lib/libavcodec.so'].toascii
toascii.restype = c_int
toascii.argtypes = [c_int]
_toupper = _libraries['/usr/local/lib/libavcodec.so']._toupper
_toupper.restype = c_int
_toupper.argtypes = [c_int]
_tolower = _libraries['/usr/local/lib/libavcodec.so']._tolower
_tolower.restype = c_int
_tolower.argtypes = [c_int]
class __locale_struct(Structure):
    pass
__locale_t = POINTER(__locale_struct)
isalnum_l = _libraries['/usr/local/lib/libavcodec.so'].isalnum_l
isalnum_l.restype = c_int
isalnum_l.argtypes = [c_int, __locale_t]
isalpha_l = _libraries['/usr/local/lib/libavcodec.so'].isalpha_l
isalpha_l.restype = c_int
isalpha_l.argtypes = [c_int, __locale_t]
iscntrl_l = _libraries['/usr/local/lib/libavcodec.so'].iscntrl_l
iscntrl_l.restype = c_int
iscntrl_l.argtypes = [c_int, __locale_t]
isdigit_l = _libraries['/usr/local/lib/libavcodec.so'].isdigit_l
isdigit_l.restype = c_int
isdigit_l.argtypes = [c_int, __locale_t]
islower_l = _libraries['/usr/local/lib/libavcodec.so'].islower_l
islower_l.restype = c_int
islower_l.argtypes = [c_int, __locale_t]
isgraph_l = _libraries['/usr/local/lib/libavcodec.so'].isgraph_l
isgraph_l.restype = c_int
isgraph_l.argtypes = [c_int, __locale_t]
isprint_l = _libraries['/usr/local/lib/libavcodec.so'].isprint_l
isprint_l.restype = c_int
isprint_l.argtypes = [c_int, __locale_t]
ispunct_l = _libraries['/usr/local/lib/libavcodec.so'].ispunct_l
ispunct_l.restype = c_int
ispunct_l.argtypes = [c_int, __locale_t]
isspace_l = _libraries['/usr/local/lib/libavcodec.so'].isspace_l
isspace_l.restype = c_int
isspace_l.argtypes = [c_int, __locale_t]
isupper_l = _libraries['/usr/local/lib/libavcodec.so'].isupper_l
isupper_l.restype = c_int
isupper_l.argtypes = [c_int, __locale_t]
isxdigit_l = _libraries['/usr/local/lib/libavcodec.so'].isxdigit_l
isxdigit_l.restype = c_int
isxdigit_l.argtypes = [c_int, __locale_t]
isblank_l = _libraries['/usr/local/lib/libavcodec.so'].isblank_l
isblank_l.restype = c_int
isblank_l.argtypes = [c_int, __locale_t]
__tolower_l = _libraries['/usr/local/lib/libavcodec.so'].__tolower_l
__tolower_l.restype = c_int
__tolower_l.argtypes = [c_int, __locale_t]
tolower_l = _libraries['/usr/local/lib/libavcodec.so'].tolower_l
tolower_l.restype = c_int
tolower_l.argtypes = [c_int, __locale_t]
__toupper_l = _libraries['/usr/local/lib/libavcodec.so'].__toupper_l
__toupper_l.restype = c_int
__toupper_l.argtypes = [c_int, __locale_t]
toupper_l = _libraries['/usr/local/lib/libavcodec.so'].toupper_l
toupper_l.restype = c_int
toupper_l.argtypes = [c_int, __locale_t]
program_invocation_short_name = (STRING).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'program_invocation_short_name')
program_invocation_name = (STRING).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'program_invocation_name')
error_t = c_int
class imaxdiv_t(Structure):
    pass
imaxdiv_t._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]
intmax_t = c_long
imaxabs = _libraries['/usr/local/lib/libavcodec.so'].imaxabs
imaxabs.restype = intmax_t
imaxabs.argtypes = [intmax_t]
imaxdiv = _libraries['/usr/local/lib/libavcodec.so'].imaxdiv
imaxdiv.restype = imaxdiv_t
imaxdiv.argtypes = [intmax_t, intmax_t]
__strtol_internal = _libraries['/usr/local/lib/libavcodec.so'].__strtol_internal
__strtol_internal.restype = c_long
__strtol_internal.argtypes = [STRING, POINTER(STRING), c_int, c_int]
strtoimax = _libraries['/usr/local/lib/libavcodec.so'].strtoimax
strtoimax.restype = intmax_t
strtoimax.argtypes = [STRING, POINTER(STRING), c_int]
__strtoul_internal = _libraries['/usr/local/lib/libavcodec.so'].__strtoul_internal
__strtoul_internal.restype = c_ulong
__strtoul_internal.argtypes = [STRING, POINTER(STRING), c_int, c_int]
uintmax_t = c_ulong
strtoumax = _libraries['/usr/local/lib/libavcodec.so'].strtoumax
strtoumax.restype = uintmax_t
strtoumax.argtypes = [STRING, POINTER(STRING), c_int]
__wcstol_internal = _libraries['/usr/local/lib/libavcodec.so'].__wcstol_internal
__wcstol_internal.restype = c_long
__wcstol_internal.argtypes = [WSTRING, POINTER(WSTRING), c_int, c_int]
wcstoimax = _libraries['/usr/local/lib/libavcodec.so'].wcstoimax
wcstoimax.restype = intmax_t
wcstoimax.argtypes = [WSTRING, POINTER(WSTRING), c_int]
__wcstoul_internal = _libraries['/usr/local/lib/libavcodec.so'].__wcstoul_internal
__wcstoul_internal.restype = c_ulong
__wcstoul_internal.argtypes = [WSTRING, POINTER(WSTRING), c_int, c_int]
wcstoumax = _libraries['/usr/local/lib/libavcodec.so'].wcstoumax
wcstoumax.restype = uintmax_t
wcstoumax.argtypes = [WSTRING, POINTER(WSTRING), c_int]
class _IO_jump_t(Structure):
    pass
_IO_jump_t._fields_ = [
]
_IO_lock_t = None
class _IO_marker(Structure):
    pass
_IO_marker._fields_ = [
    ('_next', POINTER(_IO_marker)),
    ('_sbuf', POINTER(_IO_FILE)),
    ('_pos', c_int),
]

# values for enumeration '__codecvt_result'
__codecvt_result = c_int # enum
_IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', STRING),
    ('_IO_read_end', STRING),
    ('_IO_read_base', STRING),
    ('_IO_write_base', STRING),
    ('_IO_write_ptr', STRING),
    ('_IO_write_end', STRING),
    ('_IO_buf_base', STRING),
    ('_IO_buf_end', STRING),
    ('_IO_save_base', STRING),
    ('_IO_backup_base', STRING),
    ('_IO_save_end', STRING),
    ('_markers', POINTER(_IO_marker)),
    ('_chain', POINTER(_IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_byte),
    ('_shortbuf', c_char * 1),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('__pad1', c_void_p),
    ('__pad2', c_void_p),
    ('__pad3', c_void_p),
    ('__pad4', c_void_p),
    ('__pad5', size_t),
    ('_mode', c_int),
    ('_unused2', c_char * 20),
]
class _IO_FILE_plus(Structure):
    pass
_IO_FILE_plus._fields_ = [
]
_IO_2_1_stdin_ = (_IO_FILE_plus).in_dll(_libraries['/usr/local/lib/libavcodec.so'], '_IO_2_1_stdin_')
_IO_2_1_stdout_ = (_IO_FILE_plus).in_dll(_libraries['/usr/local/lib/libavcodec.so'], '_IO_2_1_stdout_')
_IO_2_1_stderr_ = (_IO_FILE_plus).in_dll(_libraries['/usr/local/lib/libavcodec.so'], '_IO_2_1_stderr_')
__io_read_fn = CFUNCTYPE(__ssize_t, c_void_p, STRING, size_t)
__io_write_fn = CFUNCTYPE(__ssize_t, c_void_p, STRING, size_t)
__io_seek_fn = CFUNCTYPE(c_int, c_void_p, POINTER(__off64_t), c_int)
__io_close_fn = CFUNCTYPE(c_int, c_void_p)
cookie_read_function_t = __io_read_fn
cookie_write_function_t = __io_write_fn
cookie_seek_function_t = __io_seek_fn
cookie_close_function_t = __io_close_fn
class _IO_cookie_io_functions_t(Structure):
    pass
_IO_cookie_io_functions_t._fields_ = [
    ('read', POINTER(__io_read_fn)),
    ('write', POINTER(__io_write_fn)),
    ('seek', POINTER(__io_seek_fn)),
    ('close', POINTER(__io_close_fn)),
]
cookie_io_functions_t = _IO_cookie_io_functions_t
class _IO_cookie_file(Structure):
    pass
_IO_cookie_file._fields_ = [
]
__underflow = _libraries['/usr/local/lib/libavcodec.so'].__underflow
__underflow.restype = c_int
__underflow.argtypes = [POINTER(_IO_FILE)]
__uflow = _libraries['/usr/local/lib/libavcodec.so'].__uflow
__uflow.restype = c_int
__uflow.argtypes = [POINTER(_IO_FILE)]
__overflow = _libraries['/usr/local/lib/libavcodec.so'].__overflow
__overflow.restype = c_int
__overflow.argtypes = [POINTER(_IO_FILE), c_int]
_IO_getc = _libraries['/usr/local/lib/libavcodec.so']._IO_getc
_IO_getc.restype = c_int
_IO_getc.argtypes = [POINTER(_IO_FILE)]
_IO_putc = _libraries['/usr/local/lib/libavcodec.so']._IO_putc
_IO_putc.restype = c_int
_IO_putc.argtypes = [c_int, POINTER(_IO_FILE)]
_IO_feof = _libraries['/usr/local/lib/libavcodec.so']._IO_feof
_IO_feof.restype = c_int
_IO_feof.argtypes = [POINTER(_IO_FILE)]
_IO_ferror = _libraries['/usr/local/lib/libavcodec.so']._IO_ferror
_IO_ferror.restype = c_int
_IO_ferror.argtypes = [POINTER(_IO_FILE)]
_IO_peekc_locked = _libraries['/usr/local/lib/libavcodec.so']._IO_peekc_locked
_IO_peekc_locked.restype = c_int
_IO_peekc_locked.argtypes = [POINTER(_IO_FILE)]
_IO_flockfile = _libraries['/usr/local/lib/libavcodec.so']._IO_flockfile
_IO_flockfile.restype = None
_IO_flockfile.argtypes = [POINTER(_IO_FILE)]
_IO_funlockfile = _libraries['/usr/local/lib/libavcodec.so']._IO_funlockfile
_IO_funlockfile.restype = None
_IO_funlockfile.argtypes = [POINTER(_IO_FILE)]
_IO_ftrylockfile = _libraries['/usr/local/lib/libavcodec.so']._IO_ftrylockfile
_IO_ftrylockfile.restype = c_int
_IO_ftrylockfile.argtypes = [POINTER(_IO_FILE)]
_IO_vfscanf = _libraries['/usr/local/lib/libavcodec.so']._IO_vfscanf
_IO_vfscanf.restype = c_int
_IO_vfscanf.argtypes = [POINTER(_IO_FILE), STRING, POINTER(__va_list_tag), POINTER(c_int)]
_IO_vfprintf = _libraries['/usr/local/lib/libavcodec.so']._IO_vfprintf
_IO_vfprintf.restype = c_int
_IO_vfprintf.argtypes = [POINTER(_IO_FILE), STRING, POINTER(__va_list_tag)]
_IO_padn = _libraries['/usr/local/lib/libavcodec.so']._IO_padn
_IO_padn.restype = __ssize_t
_IO_padn.argtypes = [POINTER(_IO_FILE), c_int, __ssize_t]
_IO_sgetn = _libraries['/usr/local/lib/libavcodec.so']._IO_sgetn
_IO_sgetn.restype = size_t
_IO_sgetn.argtypes = [POINTER(_IO_FILE), c_void_p, size_t]
_IO_seekoff = _libraries['/usr/local/lib/libavcodec.so']._IO_seekoff
_IO_seekoff.restype = __off64_t
_IO_seekoff.argtypes = [POINTER(_IO_FILE), __off64_t, c_int, c_int]
_IO_seekpos = _libraries['/usr/local/lib/libavcodec.so']._IO_seekpos
_IO_seekpos.restype = __off64_t
_IO_seekpos.argtypes = [POINTER(_IO_FILE), __off64_t, c_int]
_IO_free_backup_area = _libraries['/usr/local/lib/libavcodec.so']._IO_free_backup_area
_IO_free_backup_area.restype = None
_IO_free_backup_area.argtypes = [POINTER(_IO_FILE)]
signgam = (c_int).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'signgam')

# values for unnamed enumeration

# values for enumeration '_LIB_VERSION_TYPE'
_LIB_VERSION_TYPE = c_int # enum
_LIB_VERSION = (_LIB_VERSION_TYPE).in_dll(_libraries['/usr/local/lib/libavcodec.so'], '_LIB_VERSION')
class __exception(Structure):
    pass
__exception._fields_ = [
    ('type', c_int),
    ('name', STRING),
    ('arg1', c_double),
    ('arg2', c_double),
    ('retval', c_double),
]
matherr = _libraries['/usr/local/lib/libavcodec.so'].matherr
matherr.restype = c_int
matherr.argtypes = [POINTER(__exception)]
int_least8_t = c_byte
int_least16_t = c_short
int_least32_t = c_int
int_least64_t = c_long
uint_least8_t = c_ubyte
uint_least16_t = c_ushort
uint_least32_t = c_uint
uint_least64_t = c_ulong
int_fast8_t = c_byte
int_fast16_t = c_long
int_fast32_t = c_long
int_fast64_t = c_long
uint_fast8_t = c_ubyte
uint_fast16_t = c_ulong
uint_fast32_t = c_ulong
uint_fast64_t = c_ulong
intptr_t = c_long
uintptr_t = c_ulong
__FILE = _IO_FILE
va_list = __gnuc_va_list
off_t = __off_t
off64_t = __off64_t
ssize_t = __ssize_t
fpos_t = _G_fpos_t
fpos64_t = _G_fpos64_t
remove = _libraries['/usr/local/lib/libavcodec.so'].remove
remove.restype = c_int
remove.argtypes = [STRING]
rename = _libraries['/usr/local/lib/libavcodec.so'].rename
rename.restype = c_int
rename.argtypes = [STRING, STRING]
renameat = _libraries['/usr/local/lib/libavcodec.so'].renameat
renameat.restype = c_int
renameat.argtypes = [c_int, STRING, c_int, STRING]
tmpfile = _libraries['/usr/local/lib/libavcodec.so'].tmpfile
tmpfile.restype = POINTER(FILE)
tmpfile.argtypes = []
tmpfile64 = _libraries['/usr/local/lib/libavcodec.so'].tmpfile64
tmpfile64.restype = POINTER(FILE)
tmpfile64.argtypes = []
tmpnam = _libraries['/usr/local/lib/libavcodec.so'].tmpnam
tmpnam.restype = STRING
tmpnam.argtypes = [STRING]
tmpnam_r = _libraries['/usr/local/lib/libavcodec.so'].tmpnam_r
tmpnam_r.restype = STRING
tmpnam_r.argtypes = [STRING]
tempnam = _libraries['/usr/local/lib/libavcodec.so'].tempnam
tempnam.restype = STRING
tempnam.argtypes = [STRING, STRING]
fclose = _libraries['/usr/local/lib/libavcodec.so'].fclose
fclose.restype = c_int
fclose.argtypes = [POINTER(FILE)]
fflush = _libraries['/usr/local/lib/libavcodec.so'].fflush
fflush.restype = c_int
fflush.argtypes = [POINTER(FILE)]
fflush_unlocked = _libraries['/usr/local/lib/libavcodec.so'].fflush_unlocked
fflush_unlocked.restype = c_int
fflush_unlocked.argtypes = [POINTER(FILE)]
fcloseall = _libraries['/usr/local/lib/libavcodec.so'].fcloseall
fcloseall.restype = c_int
fcloseall.argtypes = []
fopen = _libraries['/usr/local/lib/libavcodec.so'].fopen
fopen.restype = POINTER(FILE)
fopen.argtypes = [STRING, STRING]
freopen = _libraries['/usr/local/lib/libavcodec.so'].freopen
freopen.restype = POINTER(FILE)
freopen.argtypes = [STRING, STRING, POINTER(FILE)]
fopen64 = _libraries['/usr/local/lib/libavcodec.so'].fopen64
fopen64.restype = POINTER(FILE)
fopen64.argtypes = [STRING, STRING]
freopen64 = _libraries['/usr/local/lib/libavcodec.so'].freopen64
freopen64.restype = POINTER(FILE)
freopen64.argtypes = [STRING, STRING, POINTER(FILE)]
fdopen = _libraries['/usr/local/lib/libavcodec.so'].fdopen
fdopen.restype = POINTER(FILE)
fdopen.argtypes = [c_int, STRING]
fopencookie = _libraries['/usr/local/lib/libavcodec.so'].fopencookie
fopencookie.restype = POINTER(FILE)
fopencookie.argtypes = [c_void_p, STRING, _IO_cookie_io_functions_t]
fmemopen = _libraries['/usr/local/lib/libavcodec.so'].fmemopen
fmemopen.restype = POINTER(FILE)
fmemopen.argtypes = [c_void_p, size_t, STRING]
open_memstream = _libraries['/usr/local/lib/libavcodec.so'].open_memstream
open_memstream.restype = POINTER(FILE)
open_memstream.argtypes = [POINTER(STRING), POINTER(size_t)]
setbuf = _libraries['/usr/local/lib/libavcodec.so'].setbuf
setbuf.restype = None
setbuf.argtypes = [POINTER(FILE), STRING]
setvbuf = _libraries['/usr/local/lib/libavcodec.so'].setvbuf
setvbuf.restype = c_int
setvbuf.argtypes = [POINTER(FILE), STRING, c_int, size_t]
setbuffer = _libraries['/usr/local/lib/libavcodec.so'].setbuffer
setbuffer.restype = None
setbuffer.argtypes = [POINTER(FILE), STRING, size_t]
setlinebuf = _libraries['/usr/local/lib/libavcodec.so'].setlinebuf
setlinebuf.restype = None
setlinebuf.argtypes = [POINTER(FILE)]
fscanf = _libraries['/usr/local/lib/libavcodec.so'].fscanf
fscanf.restype = c_int
fscanf.argtypes = [POINTER(FILE), STRING]
scanf = _libraries['/usr/local/lib/libavcodec.so'].scanf
scanf.restype = c_int
scanf.argtypes = [STRING]
sscanf = _libraries['/usr/local/lib/libavcodec.so'].sscanf
sscanf.restype = c_int
sscanf.argtypes = [STRING, STRING]
vfscanf = _libraries['/usr/local/lib/libavcodec.so'].vfscanf
vfscanf.restype = c_int
vfscanf.argtypes = [POINTER(FILE), STRING, POINTER(__va_list_tag)]
vscanf = _libraries['/usr/local/lib/libavcodec.so'].vscanf
vscanf.restype = c_int
vscanf.argtypes = [STRING, POINTER(__va_list_tag)]
vsscanf = _libraries['/usr/local/lib/libavcodec.so'].vsscanf
vsscanf.restype = c_int
vsscanf.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
fgetc = _libraries['/usr/local/lib/libavcodec.so'].fgetc
fgetc.restype = c_int
fgetc.argtypes = [POINTER(FILE)]
getc = _libraries['/usr/local/lib/libavcodec.so'].getc
getc.restype = c_int
getc.argtypes = [POINTER(FILE)]
fputc = _libraries['/usr/local/lib/libavcodec.so'].fputc
fputc.restype = c_int
fputc.argtypes = [c_int, POINTER(FILE)]
putc = _libraries['/usr/local/lib/libavcodec.so'].putc
putc.restype = c_int
putc.argtypes = [c_int, POINTER(FILE)]
getw = _libraries['/usr/local/lib/libavcodec.so'].getw
getw.restype = c_int
getw.argtypes = [POINTER(FILE)]
putw = _libraries['/usr/local/lib/libavcodec.so'].putw
putw.restype = c_int
putw.argtypes = [c_int, POINTER(FILE)]
__getdelim = _libraries['/usr/local/lib/libavcodec.so'].__getdelim
__getdelim.restype = __ssize_t
__getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
getdelim = _libraries['/usr/local/lib/libavcodec.so'].getdelim
getdelim.restype = __ssize_t
getdelim.argtypes = [POINTER(STRING), POINTER(size_t), c_int, POINTER(FILE)]
fputs = _libraries['/usr/local/lib/libavcodec.so'].fputs
fputs.restype = c_int
fputs.argtypes = [STRING, POINTER(FILE)]
puts = _libraries['/usr/local/lib/libavcodec.so'].puts
puts.restype = c_int
puts.argtypes = [STRING]
ungetc = _libraries['/usr/local/lib/libavcodec.so'].ungetc
ungetc.restype = c_int
ungetc.argtypes = [c_int, POINTER(FILE)]
fwrite = _libraries['/usr/local/lib/libavcodec.so'].fwrite
fwrite.restype = size_t
fwrite.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fputs_unlocked = _libraries['/usr/local/lib/libavcodec.so'].fputs_unlocked
fputs_unlocked.restype = c_int
fputs_unlocked.argtypes = [STRING, POINTER(FILE)]
fwrite_unlocked = _libraries['/usr/local/lib/libavcodec.so'].fwrite_unlocked
fwrite_unlocked.restype = size_t
fwrite_unlocked.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
fseek = _libraries['/usr/local/lib/libavcodec.so'].fseek
fseek.restype = c_int
fseek.argtypes = [POINTER(FILE), c_long, c_int]
ftell = _libraries['/usr/local/lib/libavcodec.so'].ftell
ftell.restype = c_long
ftell.argtypes = [POINTER(FILE)]
rewind = _libraries['/usr/local/lib/libavcodec.so'].rewind
rewind.restype = None
rewind.argtypes = [POINTER(FILE)]
fseeko = _libraries['/usr/local/lib/libavcodec.so'].fseeko
fseeko.restype = c_int
fseeko.argtypes = [POINTER(FILE), __off_t, c_int]
ftello = _libraries['/usr/local/lib/libavcodec.so'].ftello
ftello.restype = __off_t
ftello.argtypes = [POINTER(FILE)]
fgetpos = _libraries['/usr/local/lib/libavcodec.so'].fgetpos
fgetpos.restype = c_int
fgetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fsetpos = _libraries['/usr/local/lib/libavcodec.so'].fsetpos
fsetpos.restype = c_int
fsetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
fseeko64 = _libraries['/usr/local/lib/libavcodec.so'].fseeko64
fseeko64.restype = c_int
fseeko64.argtypes = [POINTER(FILE), __off64_t, c_int]
ftello64 = _libraries['/usr/local/lib/libavcodec.so'].ftello64
ftello64.restype = __off64_t
ftello64.argtypes = [POINTER(FILE)]
fgetpos64 = _libraries['/usr/local/lib/libavcodec.so'].fgetpos64
fgetpos64.restype = c_int
fgetpos64.argtypes = [POINTER(FILE), POINTER(fpos64_t)]
fsetpos64 = _libraries['/usr/local/lib/libavcodec.so'].fsetpos64
fsetpos64.restype = c_int
fsetpos64.argtypes = [POINTER(FILE), POINTER(fpos64_t)]
clearerr = _libraries['/usr/local/lib/libavcodec.so'].clearerr
clearerr.restype = None
clearerr.argtypes = [POINTER(FILE)]
feof = _libraries['/usr/local/lib/libavcodec.so'].feof
feof.restype = c_int
feof.argtypes = [POINTER(FILE)]
ferror = _libraries['/usr/local/lib/libavcodec.so'].ferror
ferror.restype = c_int
ferror.argtypes = [POINTER(FILE)]
clearerr_unlocked = _libraries['/usr/local/lib/libavcodec.so'].clearerr_unlocked
clearerr_unlocked.restype = None
clearerr_unlocked.argtypes = [POINTER(FILE)]
perror = _libraries['/usr/local/lib/libavcodec.so'].perror
perror.restype = None
perror.argtypes = [STRING]
fileno = _libraries['/usr/local/lib/libavcodec.so'].fileno
fileno.restype = c_int
fileno.argtypes = [POINTER(FILE)]
fileno_unlocked = _libraries['/usr/local/lib/libavcodec.so'].fileno_unlocked
fileno_unlocked.restype = c_int
fileno_unlocked.argtypes = [POINTER(FILE)]
popen = _libraries['/usr/local/lib/libavcodec.so'].popen
popen.restype = POINTER(FILE)
popen.argtypes = [STRING, STRING]
pclose = _libraries['/usr/local/lib/libavcodec.so'].pclose
pclose.restype = c_int
pclose.argtypes = [POINTER(FILE)]
ctermid = _libraries['/usr/local/lib/libavcodec.so'].ctermid
ctermid.restype = STRING
ctermid.argtypes = [STRING]
cuserid = _libraries['/usr/local/lib/libavcodec.so'].cuserid
cuserid.restype = STRING
cuserid.argtypes = [STRING]
class obstack(Structure):
    pass
obstack._fields_ = [
]
flockfile = _libraries['/usr/local/lib/libavcodec.so'].flockfile
flockfile.restype = None
flockfile.argtypes = [POINTER(FILE)]
ftrylockfile = _libraries['/usr/local/lib/libavcodec.so'].ftrylockfile
ftrylockfile.restype = c_int
ftrylockfile.argtypes = [POINTER(FILE)]
funlockfile = _libraries['/usr/local/lib/libavcodec.so'].funlockfile
funlockfile.restype = None
funlockfile.argtypes = [POINTER(FILE)]
class div_t(Structure):
    pass
div_t._fields_ = [
    ('quot', c_int),
    ('rem', c_int),
]
class ldiv_t(Structure):
    pass
ldiv_t._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]
class lldiv_t(Structure):
    pass
lldiv_t._fields_ = [
    ('quot', c_longlong),
    ('rem', c_longlong),
]
__ctype_get_mb_cur_max = _libraries['/usr/local/lib/libavcodec.so'].__ctype_get_mb_cur_max
__ctype_get_mb_cur_max.restype = size_t
__ctype_get_mb_cur_max.argtypes = []
strtod = _libraries['/usr/local/lib/libavcodec.so'].strtod
strtod.restype = c_double
strtod.argtypes = [STRING, POINTER(STRING)]
strtof = _libraries['/usr/local/lib/libavcodec.so'].strtof
strtof.restype = c_float
strtof.argtypes = [STRING, POINTER(STRING)]
strtold = _libraries['/usr/local/lib/libavcodec.so'].strtold
strtold.restype = c_longdouble
strtold.argtypes = [STRING, POINTER(STRING)]
strtol = _libraries['/usr/local/lib/libavcodec.so'].strtol
strtol.restype = c_long
strtol.argtypes = [STRING, POINTER(STRING), c_int]
strtoul = _libraries['/usr/local/lib/libavcodec.so'].strtoul
strtoul.restype = c_ulong
strtoul.argtypes = [STRING, POINTER(STRING), c_int]
strtoq = _libraries['/usr/local/lib/libavcodec.so'].strtoq
strtoq.restype = c_longlong
strtoq.argtypes = [STRING, POINTER(STRING), c_int]
strtouq = _libraries['/usr/local/lib/libavcodec.so'].strtouq
strtouq.restype = c_ulonglong
strtouq.argtypes = [STRING, POINTER(STRING), c_int]
strtoll = _libraries['/usr/local/lib/libavcodec.so'].strtoll
strtoll.restype = c_longlong
strtoll.argtypes = [STRING, POINTER(STRING), c_int]
strtoull = _libraries['/usr/local/lib/libavcodec.so'].strtoull
strtoull.restype = c_ulonglong
strtoull.argtypes = [STRING, POINTER(STRING), c_int]
strtol_l = _libraries['/usr/local/lib/libavcodec.so'].strtol_l
strtol_l.restype = c_long
strtol_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoul_l = _libraries['/usr/local/lib/libavcodec.so'].strtoul_l
strtoul_l.restype = c_ulong
strtoul_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoll_l = _libraries['/usr/local/lib/libavcodec.so'].strtoll_l
strtoll_l.restype = c_longlong
strtoll_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoull_l = _libraries['/usr/local/lib/libavcodec.so'].strtoull_l
strtoull_l.restype = c_ulonglong
strtoull_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtod_l = _libraries['/usr/local/lib/libavcodec.so'].strtod_l
strtod_l.restype = c_double
strtod_l.argtypes = [STRING, POINTER(STRING), __locale_t]
strtof_l = _libraries['/usr/local/lib/libavcodec.so'].strtof_l
strtof_l.restype = c_float
strtof_l.argtypes = [STRING, POINTER(STRING), __locale_t]
strtold_l = _libraries['/usr/local/lib/libavcodec.so'].strtold_l
strtold_l.restype = c_longdouble
strtold_l.argtypes = [STRING, POINTER(STRING), __locale_t]
atof = _libraries['/usr/local/lib/libavcodec.so'].atof
atof.restype = c_double
atof.argtypes = [STRING]
atoi = _libraries['/usr/local/lib/libavcodec.so'].atoi
atoi.restype = c_int
atoi.argtypes = [STRING]
atol = _libraries['/usr/local/lib/libavcodec.so'].atol
atol.restype = c_long
atol.argtypes = [STRING]
atoll = _libraries['/usr/local/lib/libavcodec.so'].atoll
atoll.restype = c_longlong
atoll.argtypes = [STRING]
l64a = _libraries['/usr/local/lib/libavcodec.so'].l64a
l64a.restype = STRING
l64a.argtypes = [c_long]
a64l = _libraries['/usr/local/lib/libavcodec.so'].a64l
a64l.restype = c_long
a64l.argtypes = [STRING]
random = _libraries['/usr/local/lib/libavcodec.so'].random
random.restype = c_long
random.argtypes = []
srandom = _libraries['/usr/local/lib/libavcodec.so'].srandom
srandom.restype = None
srandom.argtypes = [c_uint]
initstate = _libraries['/usr/local/lib/libavcodec.so'].initstate
initstate.restype = STRING
initstate.argtypes = [c_uint, STRING, size_t]
setstate = _libraries['/usr/local/lib/libavcodec.so'].setstate
setstate.restype = STRING
setstate.argtypes = [STRING]
class random_data(Structure):
    pass
random_data._fields_ = [
    ('fptr', POINTER(int32_t)),
    ('rptr', POINTER(int32_t)),
    ('state', POINTER(int32_t)),
    ('rand_type', c_int),
    ('rand_deg', c_int),
    ('rand_sep', c_int),
    ('end_ptr', POINTER(int32_t)),
]
random_r = _libraries['/usr/local/lib/libavcodec.so'].random_r
random_r.restype = c_int
random_r.argtypes = [POINTER(random_data), POINTER(int32_t)]
srandom_r = _libraries['/usr/local/lib/libavcodec.so'].srandom_r
srandom_r.restype = c_int
srandom_r.argtypes = [c_uint, POINTER(random_data)]
initstate_r = _libraries['/usr/local/lib/libavcodec.so'].initstate_r
initstate_r.restype = c_int
initstate_r.argtypes = [c_uint, STRING, size_t, POINTER(random_data)]
setstate_r = _libraries['/usr/local/lib/libavcodec.so'].setstate_r
setstate_r.restype = c_int
setstate_r.argtypes = [STRING, POINTER(random_data)]
rand = _libraries['/usr/local/lib/libavcodec.so'].rand
rand.restype = c_int
rand.argtypes = []
srand = _libraries['/usr/local/lib/libavcodec.so'].srand
srand.restype = None
srand.argtypes = [c_uint]
rand_r = _libraries['/usr/local/lib/libavcodec.so'].rand_r
rand_r.restype = c_int
rand_r.argtypes = [POINTER(c_uint)]
drand48 = _libraries['/usr/local/lib/libavcodec.so'].drand48
drand48.restype = c_double
drand48.argtypes = []
erand48 = _libraries['/usr/local/lib/libavcodec.so'].erand48
erand48.restype = c_double
erand48.argtypes = [POINTER(c_ushort)]
lrand48 = _libraries['/usr/local/lib/libavcodec.so'].lrand48
lrand48.restype = c_long
lrand48.argtypes = []
nrand48 = _libraries['/usr/local/lib/libavcodec.so'].nrand48
nrand48.restype = c_long
nrand48.argtypes = [POINTER(c_ushort)]
mrand48 = _libraries['/usr/local/lib/libavcodec.so'].mrand48
mrand48.restype = c_long
mrand48.argtypes = []
jrand48 = _libraries['/usr/local/lib/libavcodec.so'].jrand48
jrand48.restype = c_long
jrand48.argtypes = [POINTER(c_ushort)]
srand48 = _libraries['/usr/local/lib/libavcodec.so'].srand48
srand48.restype = None
srand48.argtypes = [c_long]
seed48 = _libraries['/usr/local/lib/libavcodec.so'].seed48
seed48.restype = POINTER(c_ushort)
seed48.argtypes = [POINTER(c_ushort)]
lcong48 = _libraries['/usr/local/lib/libavcodec.so'].lcong48
lcong48.restype = None
lcong48.argtypes = [POINTER(c_ushort)]
class drand48_data(Structure):
    pass
drand48_data._fields_ = [
    ('__x', c_ushort * 3),
    ('__old_x', c_ushort * 3),
    ('__c', c_ushort),
    ('__init', c_ushort),
    ('__a', c_ulonglong),
]
drand48_r = _libraries['/usr/local/lib/libavcodec.so'].drand48_r
drand48_r.restype = c_int
drand48_r.argtypes = [POINTER(drand48_data), POINTER(c_double)]
erand48_r = _libraries['/usr/local/lib/libavcodec.so'].erand48_r
erand48_r.restype = c_int
erand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_double)]
lrand48_r = _libraries['/usr/local/lib/libavcodec.so'].lrand48_r
lrand48_r.restype = c_int
lrand48_r.argtypes = [POINTER(drand48_data), POINTER(c_long)]
nrand48_r = _libraries['/usr/local/lib/libavcodec.so'].nrand48_r
nrand48_r.restype = c_int
nrand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_long)]
mrand48_r = _libraries['/usr/local/lib/libavcodec.so'].mrand48_r
mrand48_r.restype = c_int
mrand48_r.argtypes = [POINTER(drand48_data), POINTER(c_long)]
jrand48_r = _libraries['/usr/local/lib/libavcodec.so'].jrand48_r
jrand48_r.restype = c_int
jrand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_long)]
srand48_r = _libraries['/usr/local/lib/libavcodec.so'].srand48_r
srand48_r.restype = c_int
srand48_r.argtypes = [c_long, POINTER(drand48_data)]
seed48_r = _libraries['/usr/local/lib/libavcodec.so'].seed48_r
seed48_r.restype = c_int
seed48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data)]
lcong48_r = _libraries['/usr/local/lib/libavcodec.so'].lcong48_r
lcong48_r.restype = c_int
lcong48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data)]
malloc = _libraries['/usr/local/lib/libavcodec.so'].malloc
malloc.restype = c_void_p
malloc.argtypes = [size_t]
calloc = _libraries['/usr/local/lib/libavcodec.so'].calloc
calloc.restype = c_void_p
calloc.argtypes = [size_t, size_t]
realloc = _libraries['/usr/local/lib/libavcodec.so'].realloc
realloc.restype = c_void_p
realloc.argtypes = [c_void_p, size_t]
free = _libraries['/usr/local/lib/libavcodec.so'].free
free.restype = None
free.argtypes = [c_void_p]
cfree = _libraries['/usr/local/lib/libavcodec.so'].cfree
cfree.restype = None
cfree.argtypes = [c_void_p]
valloc = _libraries['/usr/local/lib/libavcodec.so'].valloc
valloc.restype = c_void_p
valloc.argtypes = [size_t]
posix_memalign = _libraries['/usr/local/lib/libavcodec.so'].posix_memalign
posix_memalign.restype = c_int
posix_memalign.argtypes = [POINTER(c_void_p), size_t, size_t]
abort = _libraries['/usr/local/lib/libavcodec.so'].abort
abort.restype = None
abort.argtypes = []
on_exit = _libraries['/usr/local/lib/libavcodec.so'].on_exit
on_exit.restype = c_int
on_exit.argtypes = [CFUNCTYPE(None, c_int, c_void_p), c_void_p]
exit = _libraries['/usr/local/lib/libavcodec.so'].exit
exit.restype = None
exit.argtypes = [c_int]
quick_exit = _libraries['/usr/local/lib/libavcodec.so'].quick_exit
quick_exit.restype = None
quick_exit.argtypes = [c_int]
_Exit = _libraries['/usr/local/lib/libavcodec.so']._Exit
_Exit.restype = None
_Exit.argtypes = [c_int]
getenv = _libraries['/usr/local/lib/libavcodec.so'].getenv
getenv.restype = STRING
getenv.argtypes = [STRING]
__secure_getenv = _libraries['/usr/local/lib/libavcodec.so'].__secure_getenv
__secure_getenv.restype = STRING
__secure_getenv.argtypes = [STRING]
putenv = _libraries['/usr/local/lib/libavcodec.so'].putenv
putenv.restype = c_int
putenv.argtypes = [STRING]
setenv = _libraries['/usr/local/lib/libavcodec.so'].setenv
setenv.restype = c_int
setenv.argtypes = [STRING, STRING, c_int]
unsetenv = _libraries['/usr/local/lib/libavcodec.so'].unsetenv
unsetenv.restype = c_int
unsetenv.argtypes = [STRING]
clearenv = _libraries['/usr/local/lib/libavcodec.so'].clearenv
clearenv.restype = c_int
clearenv.argtypes = []
mktemp = _libraries['/usr/local/lib/libavcodec.so'].mktemp
mktemp.restype = STRING
mktemp.argtypes = [STRING]
mkstemp = _libraries['/usr/local/lib/libavcodec.so'].mkstemp
mkstemp.restype = c_int
mkstemp.argtypes = [STRING]
mkstemp64 = _libraries['/usr/local/lib/libavcodec.so'].mkstemp64
mkstemp64.restype = c_int
mkstemp64.argtypes = [STRING]
mkstemps = _libraries['/usr/local/lib/libavcodec.so'].mkstemps
mkstemps.restype = c_int
mkstemps.argtypes = [STRING, c_int]
mkstemps64 = _libraries['/usr/local/lib/libavcodec.so'].mkstemps64
mkstemps64.restype = c_int
mkstemps64.argtypes = [STRING, c_int]
mkdtemp = _libraries['/usr/local/lib/libavcodec.so'].mkdtemp
mkdtemp.restype = STRING
mkdtemp.argtypes = [STRING]
mkostemp = _libraries['/usr/local/lib/libavcodec.so'].mkostemp
mkostemp.restype = c_int
mkostemp.argtypes = [STRING, c_int]
mkostemp64 = _libraries['/usr/local/lib/libavcodec.so'].mkostemp64
mkostemp64.restype = c_int
mkostemp64.argtypes = [STRING, c_int]
mkostemps = _libraries['/usr/local/lib/libavcodec.so'].mkostemps
mkostemps.restype = c_int
mkostemps.argtypes = [STRING, c_int, c_int]
mkostemps64 = _libraries['/usr/local/lib/libavcodec.so'].mkostemps64
mkostemps64.restype = c_int
mkostemps64.argtypes = [STRING, c_int, c_int]
system = _libraries['/usr/local/lib/libavcodec.so'].system
system.restype = c_int
system.argtypes = [STRING]
canonicalize_file_name = _libraries['/usr/local/lib/libavcodec.so'].canonicalize_file_name
canonicalize_file_name.restype = STRING
canonicalize_file_name.argtypes = [STRING]
__compar_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p)
comparison_fn_t = __compar_fn_t
__compar_d_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)
bsearch = _libraries['/usr/local/lib/libavcodec.so'].bsearch
bsearch.restype = c_void_p
bsearch.argtypes = [c_void_p, c_void_p, size_t, size_t, __compar_fn_t]
qsort = _libraries['/usr/local/lib/libavcodec.so'].qsort
qsort.restype = None
qsort.argtypes = [c_void_p, size_t, size_t, __compar_fn_t]
qsort_r = _libraries['/usr/local/lib/libavcodec.so'].qsort_r
qsort_r.restype = None
qsort_r.argtypes = [c_void_p, size_t, size_t, __compar_d_fn_t, c_void_p]
abs = _libraries['/usr/local/lib/libavcodec.so'].abs
abs.restype = c_int
abs.argtypes = [c_int]
labs = _libraries['/usr/local/lib/libavcodec.so'].labs
labs.restype = c_long
labs.argtypes = [c_long]
llabs = _libraries['/usr/local/lib/libavcodec.so'].llabs
llabs.restype = c_longlong
llabs.argtypes = [c_longlong]
div = _libraries['/usr/local/lib/libavcodec.so'].div
div.restype = div_t
div.argtypes = [c_int, c_int]
ldiv = _libraries['/usr/local/lib/libavcodec.so'].ldiv
ldiv.restype = ldiv_t
ldiv.argtypes = [c_long, c_long]
lldiv = _libraries['/usr/local/lib/libavcodec.so'].lldiv
lldiv.restype = lldiv_t
lldiv.argtypes = [c_longlong, c_longlong]
ecvt = _libraries['/usr/local/lib/libavcodec.so'].ecvt
ecvt.restype = STRING
ecvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
fcvt = _libraries['/usr/local/lib/libavcodec.so'].fcvt
fcvt.restype = STRING
fcvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
gcvt = _libraries['/usr/local/lib/libavcodec.so'].gcvt
gcvt.restype = STRING
gcvt.argtypes = [c_double, c_int, STRING]
qecvt = _libraries['/usr/local/lib/libavcodec.so'].qecvt
qecvt.restype = STRING
qecvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
qfcvt = _libraries['/usr/local/lib/libavcodec.so'].qfcvt
qfcvt.restype = STRING
qfcvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
qgcvt = _libraries['/usr/local/lib/libavcodec.so'].qgcvt
qgcvt.restype = STRING
qgcvt.argtypes = [c_longdouble, c_int, STRING]
ecvt_r = _libraries['/usr/local/lib/libavcodec.so'].ecvt_r
ecvt_r.restype = c_int
ecvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
fcvt_r = _libraries['/usr/local/lib/libavcodec.so'].fcvt_r
fcvt_r.restype = c_int
fcvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
qecvt_r = _libraries['/usr/local/lib/libavcodec.so'].qecvt_r
qecvt_r.restype = c_int
qecvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
qfcvt_r = _libraries['/usr/local/lib/libavcodec.so'].qfcvt_r
qfcvt_r.restype = c_int
qfcvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
mblen = _libraries['/usr/local/lib/libavcodec.so'].mblen
mblen.restype = c_int
mblen.argtypes = [STRING, size_t]
mbtowc = _libraries['/usr/local/lib/libavcodec.so'].mbtowc
mbtowc.restype = c_int
mbtowc.argtypes = [WSTRING, STRING, size_t]
rpmatch = _libraries['/usr/local/lib/libavcodec.so'].rpmatch
rpmatch.restype = c_int
rpmatch.argtypes = [STRING]
getsubopt = _libraries['/usr/local/lib/libavcodec.so'].getsubopt
getsubopt.restype = c_int
getsubopt.argtypes = [POINTER(STRING), POINTER(STRING), POINTER(STRING)]
posix_openpt = _libraries['/usr/local/lib/libavcodec.so'].posix_openpt
posix_openpt.restype = c_int
posix_openpt.argtypes = [c_int]
grantpt = _libraries['/usr/local/lib/libavcodec.so'].grantpt
grantpt.restype = c_int
grantpt.argtypes = [c_int]
unlockpt = _libraries['/usr/local/lib/libavcodec.so'].unlockpt
unlockpt.restype = c_int
unlockpt.argtypes = [c_int]
ptsname = _libraries['/usr/local/lib/libavcodec.so'].ptsname
ptsname.restype = STRING
ptsname.argtypes = [c_int]
getpt = _libraries['/usr/local/lib/libavcodec.so'].getpt
getpt.restype = c_int
getpt.argtypes = []
getloadavg = _libraries['/usr/local/lib/libavcodec.so'].getloadavg
getloadavg.restype = c_int
getloadavg.argtypes = [POINTER(c_double), c_int]
memccpy = _libraries['/usr/local/lib/libavcodec.so'].memccpy
memccpy.restype = c_void_p
memccpy.argtypes = [c_void_p, c_void_p, c_int, size_t]
memcmp = _libraries['/usr/local/lib/libavcodec.so'].memcmp
memcmp.restype = c_int
memcmp.argtypes = [c_void_p, c_void_p, size_t]
memchr = _libraries['/usr/local/lib/libavcodec.so'].memchr
memchr.restype = c_void_p
memchr.argtypes = [c_void_p, c_int, size_t]
memchr = _libraries['/usr/local/lib/libavcodec.so'].memchr
memchr.restype = c_void_p
memchr.argtypes = [c_void_p, c_int, size_t]
rawmemchr = _libraries['/usr/local/lib/libavcodec.so'].rawmemchr
rawmemchr.restype = c_void_p
rawmemchr.argtypes = [c_void_p, c_int]
rawmemchr = _libraries['/usr/local/lib/libavcodec.so'].rawmemchr
rawmemchr.restype = c_void_p
rawmemchr.argtypes = [c_void_p, c_int]
memrchr = _libraries['/usr/local/lib/libavcodec.so'].memrchr
memrchr.restype = c_void_p
memrchr.argtypes = [c_void_p, c_int, size_t]
memrchr = _libraries['/usr/local/lib/libavcodec.so'].memrchr
memrchr.restype = c_void_p
memrchr.argtypes = [c_void_p, c_int, size_t]
strcmp = _libraries['/usr/local/lib/libavcodec.so'].strcmp
strcmp.restype = c_int
strcmp.argtypes = [STRING, STRING]
strncmp = _libraries['/usr/local/lib/libavcodec.so'].strncmp
strncmp.restype = c_int
strncmp.argtypes = [STRING, STRING, size_t]
strcoll = _libraries['/usr/local/lib/libavcodec.so'].strcoll
strcoll.restype = c_int
strcoll.argtypes = [STRING, STRING]
strxfrm = _libraries['/usr/local/lib/libavcodec.so'].strxfrm
strxfrm.restype = size_t
strxfrm.argtypes = [STRING, STRING, size_t]
strcoll_l = _libraries['/usr/local/lib/libavcodec.so'].strcoll_l
strcoll_l.restype = c_int
strcoll_l.argtypes = [STRING, STRING, __locale_t]
strxfrm_l = _libraries['/usr/local/lib/libavcodec.so'].strxfrm_l
strxfrm_l.restype = size_t
strxfrm_l.argtypes = [STRING, STRING, size_t, __locale_t]
strdup = _libraries['/usr/local/lib/libavcodec.so'].strdup
strdup.restype = STRING
strdup.argtypes = [STRING]
strndup = _libraries['/usr/local/lib/libavcodec.so'].strndup
strndup.restype = STRING
strndup.argtypes = [STRING, size_t]
strchr = _libraries['/usr/local/lib/libavcodec.so'].strchr
strchr.restype = STRING
strchr.argtypes = [STRING, c_int]
strchr = _libraries['/usr/local/lib/libavcodec.so'].strchr
strchr.restype = STRING
strchr.argtypes = [STRING, c_int]
strrchr = _libraries['/usr/local/lib/libavcodec.so'].strrchr
strrchr.restype = STRING
strrchr.argtypes = [STRING, c_int]
strrchr = _libraries['/usr/local/lib/libavcodec.so'].strrchr
strrchr.restype = STRING
strrchr.argtypes = [STRING, c_int]
strchrnul = _libraries['/usr/local/lib/libavcodec.so'].strchrnul
strchrnul.restype = STRING
strchrnul.argtypes = [STRING, c_int]
strchrnul = _libraries['/usr/local/lib/libavcodec.so'].strchrnul
strchrnul.restype = STRING
strchrnul.argtypes = [STRING, c_int]
strcspn = _libraries['/usr/local/lib/libavcodec.so'].strcspn
strcspn.restype = size_t
strcspn.argtypes = [STRING, STRING]
strspn = _libraries['/usr/local/lib/libavcodec.so'].strspn
strspn.restype = size_t
strspn.argtypes = [STRING, STRING]
strpbrk = _libraries['/usr/local/lib/libavcodec.so'].strpbrk
strpbrk.restype = STRING
strpbrk.argtypes = [STRING, STRING]
strpbrk = _libraries['/usr/local/lib/libavcodec.so'].strpbrk
strpbrk.restype = STRING
strpbrk.argtypes = [STRING, STRING]
strstr = _libraries['/usr/local/lib/libavcodec.so'].strstr
strstr.restype = STRING
strstr.argtypes = [STRING, STRING]
strstr = _libraries['/usr/local/lib/libavcodec.so'].strstr
strstr.restype = STRING
strstr.argtypes = [STRING, STRING]
strtok = _libraries['/usr/local/lib/libavcodec.so'].strtok
strtok.restype = STRING
strtok.argtypes = [STRING, STRING]
__strtok_r = _libraries['/usr/local/lib/libavcodec.so'].__strtok_r
__strtok_r.restype = STRING
__strtok_r.argtypes = [STRING, STRING, POINTER(STRING)]
strtok_r = _libraries['/usr/local/lib/libavcodec.so'].strtok_r
strtok_r.restype = STRING
strtok_r.argtypes = [STRING, STRING, POINTER(STRING)]
strcasestr = _libraries['/usr/local/lib/libavcodec.so'].strcasestr
strcasestr.restype = STRING
strcasestr.argtypes = [STRING, STRING]
strcasestr = _libraries['/usr/local/lib/libavcodec.so'].strcasestr
strcasestr.restype = STRING
strcasestr.argtypes = [STRING, STRING]
memmem = _libraries['/usr/local/lib/libavcodec.so'].memmem
memmem.restype = c_void_p
memmem.argtypes = [c_void_p, size_t, c_void_p, size_t]
__mempcpy = _libraries['/usr/local/lib/libavcodec.so'].__mempcpy
__mempcpy.restype = c_void_p
__mempcpy.argtypes = [c_void_p, c_void_p, size_t]
strlen = _libraries['/usr/local/lib/libavcodec.so'].strlen
strlen.restype = size_t
strlen.argtypes = [STRING]
strnlen = _libraries['/usr/local/lib/libavcodec.so'].strnlen
strnlen.restype = size_t
strnlen.argtypes = [STRING, size_t]
strerror = _libraries['/usr/local/lib/libavcodec.so'].strerror
strerror.restype = STRING
strerror.argtypes = [c_int]
strerror_r = _libraries['/usr/local/lib/libavcodec.so'].strerror_r
strerror_r.restype = STRING
strerror_r.argtypes = [c_int, STRING, size_t]
strerror_l = _libraries['/usr/local/lib/libavcodec.so'].strerror_l
strerror_l.restype = STRING
strerror_l.argtypes = [c_int, __locale_t]
__bzero = _libraries['/usr/local/lib/libavcodec.so'].__bzero
__bzero.restype = None
__bzero.argtypes = [c_void_p, size_t]
bcmp = _libraries['/usr/local/lib/libavcodec.so'].bcmp
bcmp.restype = c_int
bcmp.argtypes = [c_void_p, c_void_p, size_t]
index = _libraries['/usr/local/lib/libavcodec.so'].index
index.restype = STRING
index.argtypes = [STRING, c_int]
index = _libraries['/usr/local/lib/libavcodec.so'].index
index.restype = STRING
index.argtypes = [STRING, c_int]
rindex = _libraries['/usr/local/lib/libavcodec.so'].rindex
rindex.restype = STRING
rindex.argtypes = [STRING, c_int]
rindex = _libraries['/usr/local/lib/libavcodec.so'].rindex
rindex.restype = STRING
rindex.argtypes = [STRING, c_int]
ffs = _libraries['/usr/local/lib/libavcodec.so'].ffs
ffs.restype = c_int
ffs.argtypes = [c_int]
ffsl = _libraries['/usr/local/lib/libavcodec.so'].ffsl
ffsl.restype = c_int
ffsl.argtypes = [c_long]
ffsll = _libraries['/usr/local/lib/libavcodec.so'].ffsll
ffsll.restype = c_int
ffsll.argtypes = [c_longlong]
strcasecmp = _libraries['/usr/local/lib/libavcodec.so'].strcasecmp
strcasecmp.restype = c_int
strcasecmp.argtypes = [STRING, STRING]
strncasecmp = _libraries['/usr/local/lib/libavcodec.so'].strncasecmp
strncasecmp.restype = c_int
strncasecmp.argtypes = [STRING, STRING, size_t]
strcasecmp_l = _libraries['/usr/local/lib/libavcodec.so'].strcasecmp_l
strcasecmp_l.restype = c_int
strcasecmp_l.argtypes = [STRING, STRING, __locale_t]
strncasecmp_l = _libraries['/usr/local/lib/libavcodec.so'].strncasecmp_l
strncasecmp_l.restype = c_int
strncasecmp_l.argtypes = [STRING, STRING, size_t, __locale_t]
strsep = _libraries['/usr/local/lib/libavcodec.so'].strsep
strsep.restype = STRING
strsep.argtypes = [POINTER(STRING), STRING]
strsignal = _libraries['/usr/local/lib/libavcodec.so'].strsignal
strsignal.restype = STRING
strsignal.argtypes = [c_int]
__stpcpy = _libraries['/usr/local/lib/libavcodec.so'].__stpcpy
__stpcpy.restype = STRING
__stpcpy.argtypes = [STRING, STRING]
__stpncpy = _libraries['/usr/local/lib/libavcodec.so'].__stpncpy
__stpncpy.restype = STRING
__stpncpy.argtypes = [STRING, STRING, size_t]
strverscmp = _libraries['/usr/local/lib/libavcodec.so'].strverscmp
strverscmp.restype = c_int
strverscmp.argtypes = [STRING, STRING]
strfry = _libraries['/usr/local/lib/libavcodec.so'].strfry
strfry.restype = STRING
strfry.argtypes = [STRING]
memfrob = _libraries['/usr/local/lib/libavcodec.so'].memfrob
memfrob.restype = c_void_p
memfrob.argtypes = [c_void_p, size_t]
basename = _libraries['/usr/local/lib/libavcodec.so'].basename
basename.restype = STRING
basename.argtypes = [STRING]
basename = _libraries['/usr/local/lib/libavcodec.so'].basename
basename.restype = STRING
basename.argtypes = [STRING]
__clock_t = c_long
clock_t = __clock_t
__time_t = c_long
time_t = __time_t
__clockid_t = c_int
clockid_t = __clockid_t
__timer_t = c_void_p
timer_t = __timer_t
class timespec(Structure):
    pass
timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', c_long),
]
class tm(Structure):
    pass
tm._fields_ = [
    ('tm_sec', c_int),
    ('tm_min', c_int),
    ('tm_hour', c_int),
    ('tm_mday', c_int),
    ('tm_mon', c_int),
    ('tm_year', c_int),
    ('tm_wday', c_int),
    ('tm_yday', c_int),
    ('tm_isdst', c_int),
    ('tm_gmtoff', c_long),
    ('tm_zone', STRING),
]
class itimerspec(Structure):
    pass
itimerspec._fields_ = [
    ('it_interval', timespec),
    ('it_value', timespec),
]
class sigevent(Structure):
    pass
sigevent._fields_ = [
]
clock = _libraries['/usr/local/lib/libavcodec.so'].clock
clock.restype = clock_t
clock.argtypes = []
time = _libraries['/usr/local/lib/libavcodec.so'].time
time.restype = time_t
time.argtypes = [POINTER(time_t)]
difftime = _libraries['/usr/local/lib/libavcodec.so'].difftime
difftime.restype = c_double
difftime.argtypes = [time_t, time_t]
mktime = _libraries['/usr/local/lib/libavcodec.so'].mktime
mktime.restype = time_t
mktime.argtypes = [POINTER(tm)]
strftime = _libraries['/usr/local/lib/libavcodec.so'].strftime
strftime.restype = size_t
strftime.argtypes = [STRING, size_t, STRING, POINTER(tm)]
strptime = _libraries['/usr/local/lib/libavcodec.so'].strptime
strptime.restype = STRING
strptime.argtypes = [STRING, STRING, POINTER(tm)]
strftime_l = _libraries['/usr/local/lib/libavcodec.so'].strftime_l
strftime_l.restype = size_t
strftime_l.argtypes = [STRING, size_t, STRING, POINTER(tm), __locale_t]
strptime_l = _libraries['/usr/local/lib/libavcodec.so'].strptime_l
strptime_l.restype = STRING
strptime_l.argtypes = [STRING, STRING, POINTER(tm), __locale_t]
gmtime = _libraries['/usr/local/lib/libavcodec.so'].gmtime
gmtime.restype = POINTER(tm)
gmtime.argtypes = [POINTER(time_t)]
localtime = _libraries['/usr/local/lib/libavcodec.so'].localtime
localtime.restype = POINTER(tm)
localtime.argtypes = [POINTER(time_t)]
gmtime_r = _libraries['/usr/local/lib/libavcodec.so'].gmtime_r
gmtime_r.restype = POINTER(tm)
gmtime_r.argtypes = [POINTER(time_t), POINTER(tm)]
localtime_r = _libraries['/usr/local/lib/libavcodec.so'].localtime_r
localtime_r.restype = POINTER(tm)
localtime_r.argtypes = [POINTER(time_t), POINTER(tm)]
asctime = _libraries['/usr/local/lib/libavcodec.so'].asctime
asctime.restype = STRING
asctime.argtypes = [POINTER(tm)]
ctime = _libraries['/usr/local/lib/libavcodec.so'].ctime
ctime.restype = STRING
ctime.argtypes = [POINTER(time_t)]
asctime_r = _libraries['/usr/local/lib/libavcodec.so'].asctime_r
asctime_r.restype = STRING
asctime_r.argtypes = [POINTER(tm), STRING]
ctime_r = _libraries['/usr/local/lib/libavcodec.so'].ctime_r
ctime_r.restype = STRING
ctime_r.argtypes = [POINTER(time_t), STRING]
__tzname = (STRING * 2).in_dll(_libraries['/usr/local/lib/libavcodec.so'], '__tzname')
__daylight = (c_int).in_dll(_libraries['/usr/local/lib/libavcodec.so'], '__daylight')
__timezone = (c_long).in_dll(_libraries['/usr/local/lib/libavcodec.so'], '__timezone')
tzname = (STRING * 2).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'tzname')
tzset = _libraries['/usr/local/lib/libavcodec.so'].tzset
tzset.restype = None
tzset.argtypes = []
daylight = (c_int).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'daylight')
timezone = (c_long).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'timezone')
stime = _libraries['/usr/local/lib/libavcodec.so'].stime
stime.restype = c_int
stime.argtypes = [POINTER(time_t)]
timegm = _libraries['/usr/local/lib/libavcodec.so'].timegm
timegm.restype = time_t
timegm.argtypes = [POINTER(tm)]
timelocal = _libraries['/usr/local/lib/libavcodec.so'].timelocal
timelocal.restype = time_t
timelocal.argtypes = [POINTER(tm)]
dysize = _libraries['/usr/local/lib/libavcodec.so'].dysize
dysize.restype = c_int
dysize.argtypes = [c_int]
nanosleep = _libraries['/usr/local/lib/libavcodec.so'].nanosleep
nanosleep.restype = c_int
nanosleep.argtypes = [POINTER(timespec), POINTER(timespec)]
clock_getres = _libraries['/usr/local/lib/libavdevice.so'].clock_getres
clock_getres.restype = c_int
clock_getres.argtypes = [clockid_t, POINTER(timespec)]
clock_gettime = _libraries['/usr/local/lib/libavdevice.so'].clock_gettime
clock_gettime.restype = c_int
clock_gettime.argtypes = [clockid_t, POINTER(timespec)]
clock_settime = _libraries['/usr/local/lib/libavdevice.so'].clock_settime
clock_settime.restype = c_int
clock_settime.argtypes = [clockid_t, POINTER(timespec)]
clock_nanosleep = _libraries['/usr/local/lib/libavdevice.so'].clock_nanosleep
clock_nanosleep.restype = c_int
clock_nanosleep.argtypes = [clockid_t, c_int, POINTER(timespec), POINTER(timespec)]
pid_t = __pid_t
clock_getcpuclockid = _libraries['/usr/local/lib/libavdevice.so'].clock_getcpuclockid
clock_getcpuclockid.restype = c_int
clock_getcpuclockid.argtypes = [pid_t, POINTER(clockid_t)]
timer_create = _libraries['/usr/local/lib/libavdevice.so'].timer_create
timer_create.restype = c_int
timer_create.argtypes = [clockid_t, POINTER(sigevent), POINTER(timer_t)]
timer_delete = _libraries['/usr/local/lib/libavdevice.so'].timer_delete
timer_delete.restype = c_int
timer_delete.argtypes = [timer_t]
timer_settime = _libraries['/usr/local/lib/libavdevice.so'].timer_settime
timer_settime.restype = c_int
timer_settime.argtypes = [timer_t, c_int, POINTER(itimerspec), POINTER(itimerspec)]
timer_gettime = _libraries['/usr/local/lib/libavdevice.so'].timer_gettime
timer_gettime.restype = c_int
timer_gettime.argtypes = [timer_t, POINTER(itimerspec)]
timer_getoverrun = _libraries['/usr/local/lib/libavdevice.so'].timer_getoverrun
timer_getoverrun.restype = c_int
timer_getoverrun.argtypes = [timer_t]
getdate_err = (c_int).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'getdate_err')
getdate = _libraries['/usr/local/lib/libavcodec.so'].getdate
getdate.restype = POINTER(tm)
getdate.argtypes = [STRING]
getdate_r = _libraries['/usr/local/lib/libavcodec.so'].getdate_r
getdate_r.restype = c_int
getdate_r.argtypes = [STRING, POINTER(tm)]
__errno_location = _libraries['/usr/local/lib/libavcodec.so'].__errno_location
__errno_location.restype = POINTER(c_int)
__errno_location.argtypes = []
acosf = _libraries['/usr/local/lib/libavcodec.so'].acosf
acosf.restype = c_float
acosf.argtypes = [c_float]
acosl = _libraries['/usr/local/lib/libavcodec.so'].acosl
acosl.restype = c_longdouble
acosl.argtypes = [c_longdouble]
acos = _libraries['/usr/local/lib/libavcodec.so'].acos
acos.restype = c_double
acos.argtypes = [c_double]
asinl = _libraries['/usr/local/lib/libavcodec.so'].asinl
asinl.restype = c_longdouble
asinl.argtypes = [c_longdouble]
asin = _libraries['/usr/local/lib/libavcodec.so'].asin
asin.restype = c_double
asin.argtypes = [c_double]
asinf = _libraries['/usr/local/lib/libavcodec.so'].asinf
asinf.restype = c_float
asinf.argtypes = [c_float]
atanl = _libraries['/usr/local/lib/libavcodec.so'].atanl
atanl.restype = c_longdouble
atanl.argtypes = [c_longdouble]
atanf = _libraries['/usr/local/lib/libavcodec.so'].atanf
atanf.restype = c_float
atanf.argtypes = [c_float]
atan = _libraries['/usr/local/lib/libavcodec.so'].atan
atan.restype = c_double
atan.argtypes = [c_double]
atan2f = _libraries['/usr/local/lib/libavcodec.so'].atan2f
atan2f.restype = c_float
atan2f.argtypes = [c_float, c_float]
atan2l = _libraries['/usr/local/lib/libavcodec.so'].atan2l
atan2l.restype = c_longdouble
atan2l.argtypes = [c_longdouble, c_longdouble]
atan2 = _libraries['/usr/local/lib/libavcodec.so'].atan2
atan2.restype = c_double
atan2.argtypes = [c_double, c_double]
cos = _libraries['/usr/local/lib/libavcodec.so'].cos
cos.restype = c_double
cos.argtypes = [c_double]
cosf = _libraries['/usr/local/lib/libavcodec.so'].cosf
cosf.restype = c_float
cosf.argtypes = [c_float]
cosl = _libraries['/usr/local/lib/libavcodec.so'].cosl
cosl.restype = c_longdouble
cosl.argtypes = [c_longdouble]
sinf = _libraries['/usr/local/lib/libavcodec.so'].sinf
sinf.restype = c_float
sinf.argtypes = [c_float]
sin = _libraries['/usr/local/lib/libavcodec.so'].sin
sin.restype = c_double
sin.argtypes = [c_double]
sinl = _libraries['/usr/local/lib/libavcodec.so'].sinl
sinl.restype = c_longdouble
sinl.argtypes = [c_longdouble]
tanf = _libraries['/usr/local/lib/libavcodec.so'].tanf
tanf.restype = c_float
tanf.argtypes = [c_float]
tanl = _libraries['/usr/local/lib/libavcodec.so'].tanl
tanl.restype = c_longdouble
tanl.argtypes = [c_longdouble]
tan = _libraries['/usr/local/lib/libavcodec.so'].tan
tan.restype = c_double
tan.argtypes = [c_double]
cosh = _libraries['/usr/local/lib/libavcodec.so'].cosh
cosh.restype = c_double
cosh.argtypes = [c_double]
coshf = _libraries['/usr/local/lib/libavcodec.so'].coshf
coshf.restype = c_float
coshf.argtypes = [c_float]
coshl = _libraries['/usr/local/lib/libavcodec.so'].coshl
coshl.restype = c_longdouble
coshl.argtypes = [c_longdouble]
sinhl = _libraries['/usr/local/lib/libavcodec.so'].sinhl
sinhl.restype = c_longdouble
sinhl.argtypes = [c_longdouble]
sinhf = _libraries['/usr/local/lib/libavcodec.so'].sinhf
sinhf.restype = c_float
sinhf.argtypes = [c_float]
sinh = _libraries['/usr/local/lib/libavcodec.so'].sinh
sinh.restype = c_double
sinh.argtypes = [c_double]
tanh = _libraries['/usr/local/lib/libavcodec.so'].tanh
tanh.restype = c_double
tanh.argtypes = [c_double]
tanhf = _libraries['/usr/local/lib/libavcodec.so'].tanhf
tanhf.restype = c_float
tanhf.argtypes = [c_float]
tanhl = _libraries['/usr/local/lib/libavcodec.so'].tanhl
tanhl.restype = c_longdouble
tanhl.argtypes = [c_longdouble]
sincosf = _libraries['/usr/local/lib/libavcodec.so'].sincosf
sincosf.restype = None
sincosf.argtypes = [c_float, POINTER(c_float), POINTER(c_float)]
sincosl = _libraries['/usr/local/lib/libavcodec.so'].sincosl
sincosl.restype = None
sincosl.argtypes = [c_longdouble, POINTER(c_longdouble), POINTER(c_longdouble)]
sincos = _libraries['/usr/local/lib/libavcodec.so'].sincos
sincos.restype = None
sincos.argtypes = [c_double, POINTER(c_double), POINTER(c_double)]
acoshl = _libraries['/usr/local/lib/libavcodec.so'].acoshl
acoshl.restype = c_longdouble
acoshl.argtypes = [c_longdouble]
acosh = _libraries['/usr/local/lib/libavcodec.so'].acosh
acosh.restype = c_double
acosh.argtypes = [c_double]
acoshf = _libraries['/usr/local/lib/libavcodec.so'].acoshf
acoshf.restype = c_float
acoshf.argtypes = [c_float]
asinh = _libraries['/usr/local/lib/libavcodec.so'].asinh
asinh.restype = c_double
asinh.argtypes = [c_double]
asinhf = _libraries['/usr/local/lib/libavcodec.so'].asinhf
asinhf.restype = c_float
asinhf.argtypes = [c_float]
asinhl = _libraries['/usr/local/lib/libavcodec.so'].asinhl
asinhl.restype = c_longdouble
asinhl.argtypes = [c_longdouble]
atanhf = _libraries['/usr/local/lib/libavcodec.so'].atanhf
atanhf.restype = c_float
atanhf.argtypes = [c_float]
atanh = _libraries['/usr/local/lib/libavcodec.so'].atanh
atanh.restype = c_double
atanh.argtypes = [c_double]
atanhl = _libraries['/usr/local/lib/libavcodec.so'].atanhl
atanhl.restype = c_longdouble
atanhl.argtypes = [c_longdouble]
expf = _libraries['/usr/local/lib/libavcodec.so'].expf
expf.restype = c_float
expf.argtypes = [c_float]
exp = _libraries['/usr/local/lib/libavcodec.so'].exp
exp.restype = c_double
exp.argtypes = [c_double]
expl = _libraries['/usr/local/lib/libavcodec.so'].expl
expl.restype = c_longdouble
expl.argtypes = [c_longdouble]
frexpf = _libraries['/usr/local/lib/libavcodec.so'].frexpf
frexpf.restype = c_float
frexpf.argtypes = [c_float, POINTER(c_int)]
frexpl = _libraries['/usr/local/lib/libavcodec.so'].frexpl
frexpl.restype = c_longdouble
frexpl.argtypes = [c_longdouble, POINTER(c_int)]
frexp = _libraries['/usr/local/lib/libavcodec.so'].frexp
frexp.restype = c_double
frexp.argtypes = [c_double, POINTER(c_int)]
ldexpf = _libraries['/usr/local/lib/libavcodec.so'].ldexpf
ldexpf.restype = c_float
ldexpf.argtypes = [c_float, c_int]
ldexpl = _libraries['/usr/local/lib/libavcodec.so'].ldexpl
ldexpl.restype = c_longdouble
ldexpl.argtypes = [c_longdouble, c_int]
ldexp = _libraries['/usr/local/lib/libavcodec.so'].ldexp
ldexp.restype = c_double
ldexp.argtypes = [c_double, c_int]
log = _libraries['/usr/local/lib/libavcodec.so'].log
log.restype = c_double
log.argtypes = [c_double]
logf = _libraries['/usr/local/lib/libavcodec.so'].logf
logf.restype = c_float
logf.argtypes = [c_float]
logl = _libraries['/usr/local/lib/libavcodec.so'].logl
logl.restype = c_longdouble
logl.argtypes = [c_longdouble]
log10f = _libraries['/usr/local/lib/libavcodec.so'].log10f
log10f.restype = c_float
log10f.argtypes = [c_float]
log10l = _libraries['/usr/local/lib/libavcodec.so'].log10l
log10l.restype = c_longdouble
log10l.argtypes = [c_longdouble]
log10 = _libraries['/usr/local/lib/libavcodec.so'].log10
log10.restype = c_double
log10.argtypes = [c_double]
modff = _libraries['/usr/local/lib/libavcodec.so'].modff
modff.restype = c_float
modff.argtypes = [c_float, POINTER(c_float)]
modf = _libraries['/usr/local/lib/libavcodec.so'].modf
modf.restype = c_double
modf.argtypes = [c_double, POINTER(c_double)]
modfl = _libraries['/usr/local/lib/libavcodec.so'].modfl
modfl.restype = c_longdouble
modfl.argtypes = [c_longdouble, POINTER(c_longdouble)]
exp10l = _libraries['/usr/local/lib/libavcodec.so'].exp10l
exp10l.restype = c_longdouble
exp10l.argtypes = [c_longdouble]
exp10f = _libraries['/usr/local/lib/libavcodec.so'].exp10f
exp10f.restype = c_float
exp10f.argtypes = [c_float]
exp10 = _libraries['/usr/local/lib/libavcodec.so'].exp10
exp10.restype = c_double
exp10.argtypes = [c_double]
pow10l = _libraries['/usr/local/lib/libavcodec.so'].pow10l
pow10l.restype = c_longdouble
pow10l.argtypes = [c_longdouble]
pow10 = _libraries['/usr/local/lib/libavcodec.so'].pow10
pow10.restype = c_double
pow10.argtypes = [c_double]
pow10f = _libraries['/usr/local/lib/libavcodec.so'].pow10f
pow10f.restype = c_float
pow10f.argtypes = [c_float]
expm1l = _libraries['/usr/local/lib/libavcodec.so'].expm1l
expm1l.restype = c_longdouble
expm1l.argtypes = [c_longdouble]
expm1f = _libraries['/usr/local/lib/libavcodec.so'].expm1f
expm1f.restype = c_float
expm1f.argtypes = [c_float]
expm1 = _libraries['/usr/local/lib/libavcodec.so'].expm1
expm1.restype = c_double
expm1.argtypes = [c_double]
log1pl = _libraries['/usr/local/lib/libavcodec.so'].log1pl
log1pl.restype = c_longdouble
log1pl.argtypes = [c_longdouble]
log1pf = _libraries['/usr/local/lib/libavcodec.so'].log1pf
log1pf.restype = c_float
log1pf.argtypes = [c_float]
log1p = _libraries['/usr/local/lib/libavcodec.so'].log1p
log1p.restype = c_double
log1p.argtypes = [c_double]
logbf = _libraries['/usr/local/lib/libavcodec.so'].logbf
logbf.restype = c_float
logbf.argtypes = [c_float]
logbl = _libraries['/usr/local/lib/libavcodec.so'].logbl
logbl.restype = c_longdouble
logbl.argtypes = [c_longdouble]
logb = _libraries['/usr/local/lib/libavcodec.so'].logb
logb.restype = c_double
logb.argtypes = [c_double]
exp2 = _libraries['/usr/local/lib/libavcodec.so'].exp2
exp2.restype = c_double
exp2.argtypes = [c_double]
exp2l = _libraries['/usr/local/lib/libavcodec.so'].exp2l
exp2l.restype = c_longdouble
exp2l.argtypes = [c_longdouble]
exp2f = _libraries['/usr/local/lib/libavcodec.so'].exp2f
exp2f.restype = c_float
exp2f.argtypes = [c_float]
log2 = _libraries['/usr/local/lib/libavcodec.so'].log2
log2.restype = c_double
log2.argtypes = [c_double]
log2l = _libraries['/usr/local/lib/libavcodec.so'].log2l
log2l.restype = c_longdouble
log2l.argtypes = [c_longdouble]
log2f = _libraries['/usr/local/lib/libavcodec.so'].log2f
log2f.restype = c_float
log2f.argtypes = [c_float]
powl = _libraries['/usr/local/lib/libavcodec.so'].powl
powl.restype = c_longdouble
powl.argtypes = [c_longdouble, c_longdouble]
pow = _libraries['/usr/local/lib/libavcodec.so'].pow
pow.restype = c_double
pow.argtypes = [c_double, c_double]
powf = _libraries['/usr/local/lib/libavcodec.so'].powf
powf.restype = c_float
powf.argtypes = [c_float, c_float]
sqrtl = _libraries['/usr/local/lib/libavcodec.so'].sqrtl
sqrtl.restype = c_longdouble
sqrtl.argtypes = [c_longdouble]
sqrt = _libraries['/usr/local/lib/libavcodec.so'].sqrt
sqrt.restype = c_double
sqrt.argtypes = [c_double]
sqrtf = _libraries['/usr/local/lib/libavcodec.so'].sqrtf
sqrtf.restype = c_float
sqrtf.argtypes = [c_float]
hypot = _libraries['/usr/local/lib/libavcodec.so'].hypot
hypot.restype = c_double
hypot.argtypes = [c_double, c_double]
hypotf = _libraries['/usr/local/lib/libavcodec.so'].hypotf
hypotf.restype = c_float
hypotf.argtypes = [c_float, c_float]
hypotl = _libraries['/usr/local/lib/libavcodec.so'].hypotl
hypotl.restype = c_longdouble
hypotl.argtypes = [c_longdouble, c_longdouble]
cbrtl = _libraries['/usr/local/lib/libavcodec.so'].cbrtl
cbrtl.restype = c_longdouble
cbrtl.argtypes = [c_longdouble]
cbrtf = _libraries['/usr/local/lib/libavcodec.so'].cbrtf
cbrtf.restype = c_float
cbrtf.argtypes = [c_float]
cbrt = _libraries['/usr/local/lib/libavcodec.so'].cbrt
cbrt.restype = c_double
cbrt.argtypes = [c_double]
ceill = _libraries['/usr/local/lib/libavcodec.so'].ceill
ceill.restype = c_longdouble
ceill.argtypes = [c_longdouble]
ceil = _libraries['/usr/local/lib/libavcodec.so'].ceil
ceil.restype = c_double
ceil.argtypes = [c_double]
ceilf = _libraries['/usr/local/lib/libavcodec.so'].ceilf
ceilf.restype = c_float
ceilf.argtypes = [c_float]
fabs = _libraries['/usr/local/lib/libavcodec.so'].fabs
fabs.restype = c_double
fabs.argtypes = [c_double]
fabsf = _libraries['/usr/local/lib/libavcodec.so'].fabsf
fabsf.restype = c_float
fabsf.argtypes = [c_float]
fabsl = _libraries['/usr/local/lib/libavcodec.so'].fabsl
fabsl.restype = c_longdouble
fabsl.argtypes = [c_longdouble]
floorl = _libraries['/usr/local/lib/libavcodec.so'].floorl
floorl.restype = c_longdouble
floorl.argtypes = [c_longdouble]
floor = _libraries['/usr/local/lib/libavcodec.so'].floor
floor.restype = c_double
floor.argtypes = [c_double]
floorf = _libraries['/usr/local/lib/libavcodec.so'].floorf
floorf.restype = c_float
floorf.argtypes = [c_float]
fmodl = _libraries['/usr/local/lib/libavcodec.so'].fmodl
fmodl.restype = c_longdouble
fmodl.argtypes = [c_longdouble, c_longdouble]
fmod = _libraries['/usr/local/lib/libavcodec.so'].fmod
fmod.restype = c_double
fmod.argtypes = [c_double, c_double]
fmodf = _libraries['/usr/local/lib/libavcodec.so'].fmodf
fmodf.restype = c_float
fmodf.argtypes = [c_float, c_float]
__isinf = _libraries['/usr/local/lib/libavcodec.so'].__isinf
__isinf.restype = c_int
__isinf.argtypes = [c_double]
__isinff = _libraries['/usr/local/lib/libavcodec.so'].__isinff
__isinff.restype = c_int
__isinff.argtypes = [c_float]
__isinfl = _libraries['/usr/local/lib/libavcodec.so'].__isinfl
__isinfl.restype = c_int
__isinfl.argtypes = [c_longdouble]
__finitef = _libraries['/usr/local/lib/libavcodec.so'].__finitef
__finitef.restype = c_int
__finitef.argtypes = [c_float]
__finitel = _libraries['/usr/local/lib/libavcodec.so'].__finitel
__finitel.restype = c_int
__finitel.argtypes = [c_longdouble]
__finite = _libraries['/usr/local/lib/libavcodec.so'].__finite
__finite.restype = c_int
__finite.argtypes = [c_double]
isinfl = _libraries['/usr/local/lib/libavcodec.so'].isinfl
isinfl.restype = c_int
isinfl.argtypes = [c_longdouble]
isinf = _libraries['/usr/local/lib/libavcodec.so'].isinf
isinf.restype = c_int
isinf.argtypes = [c_double]
isinff = _libraries['/usr/local/lib/libavcodec.so'].isinff
isinff.restype = c_int
isinff.argtypes = [c_float]
finitef = _libraries['/usr/local/lib/libavcodec.so'].finitef
finitef.restype = c_int
finitef.argtypes = [c_float]
finite = _libraries['/usr/local/lib/libavcodec.so'].finite
finite.restype = c_int
finite.argtypes = [c_double]
finitel = _libraries['/usr/local/lib/libavcodec.so'].finitel
finitel.restype = c_int
finitel.argtypes = [c_longdouble]
dremf = _libraries['/usr/local/lib/libavcodec.so'].dremf
dremf.restype = c_float
dremf.argtypes = [c_float, c_float]
drem = _libraries['/usr/local/lib/libavcodec.so'].drem
drem.restype = c_double
drem.argtypes = [c_double, c_double]
dreml = _libraries['/usr/local/lib/libavcodec.so'].dreml
dreml.restype = c_longdouble
dreml.argtypes = [c_longdouble, c_longdouble]
significandf = _libraries['/usr/local/lib/libavcodec.so'].significandf
significandf.restype = c_float
significandf.argtypes = [c_float]
significandl = _libraries['/usr/local/lib/libavcodec.so'].significandl
significandl.restype = c_longdouble
significandl.argtypes = [c_longdouble]
significand = _libraries['/usr/local/lib/libavcodec.so'].significand
significand.restype = c_double
significand.argtypes = [c_double]
copysign = _libraries['/usr/local/lib/libavcodec.so'].copysign
copysign.restype = c_double
copysign.argtypes = [c_double, c_double]
copysignf = _libraries['/usr/local/lib/libavcodec.so'].copysignf
copysignf.restype = c_float
copysignf.argtypes = [c_float, c_float]
copysignl = _libraries['/usr/local/lib/libavcodec.so'].copysignl
copysignl.restype = c_longdouble
copysignl.argtypes = [c_longdouble, c_longdouble]
nanf = _libraries['/usr/local/lib/libavcodec.so'].nanf
nanf.restype = c_float
nanf.argtypes = [STRING]
nanl = _libraries['/usr/local/lib/libavcodec.so'].nanl
nanl.restype = c_longdouble
nanl.argtypes = [STRING]
nan = _libraries['/usr/local/lib/libavcodec.so'].nan
nan.restype = c_double
nan.argtypes = [STRING]
__isnan = _libraries['/usr/local/lib/libavcodec.so'].__isnan
__isnan.restype = c_int
__isnan.argtypes = [c_double]
__isnanf = _libraries['/usr/local/lib/libavcodec.so'].__isnanf
__isnanf.restype = c_int
__isnanf.argtypes = [c_float]
__isnanl = _libraries['/usr/local/lib/libavcodec.so'].__isnanl
__isnanl.restype = c_int
__isnanl.argtypes = [c_longdouble]
isnanf = _libraries['/usr/local/lib/libavcodec.so'].isnanf
isnanf.restype = c_int
isnanf.argtypes = [c_float]
isnan = _libraries['/usr/local/lib/libavcodec.so'].isnan
isnan.restype = c_int
isnan.argtypes = [c_double]
isnanl = _libraries['/usr/local/lib/libavcodec.so'].isnanl
isnanl.restype = c_int
isnanl.argtypes = [c_longdouble]
j0f = _libraries['/usr/local/lib/libavcodec.so'].j0f
j0f.restype = c_float
j0f.argtypes = [c_float]
j0l = _libraries['/usr/local/lib/libavcodec.so'].j0l
j0l.restype = c_longdouble
j0l.argtypes = [c_longdouble]
j0 = _libraries['/usr/local/lib/libavcodec.so'].j0
j0.restype = c_double
j0.argtypes = [c_double]
j1l = _libraries['/usr/local/lib/libavcodec.so'].j1l
j1l.restype = c_longdouble
j1l.argtypes = [c_longdouble]
j1f = _libraries['/usr/local/lib/libavcodec.so'].j1f
j1f.restype = c_float
j1f.argtypes = [c_float]
j1 = _libraries['/usr/local/lib/libavcodec.so'].j1
j1.restype = c_double
j1.argtypes = [c_double]
jnf = _libraries['/usr/local/lib/libavcodec.so'].jnf
jnf.restype = c_float
jnf.argtypes = [c_int, c_float]
jnl = _libraries['/usr/local/lib/libavcodec.so'].jnl
jnl.restype = c_longdouble
jnl.argtypes = [c_int, c_longdouble]
jn = _libraries['/usr/local/lib/libavcodec.so'].jn
jn.restype = c_double
jn.argtypes = [c_int, c_double]
y0f = _libraries['/usr/local/lib/libavcodec.so'].y0f
y0f.restype = c_float
y0f.argtypes = [c_float]
y0l = _libraries['/usr/local/lib/libavcodec.so'].y0l
y0l.restype = c_longdouble
y0l.argtypes = [c_longdouble]
y0 = _libraries['/usr/local/lib/libavcodec.so'].y0
y0.restype = c_double
y0.argtypes = [c_double]
y1f = _libraries['/usr/local/lib/libavcodec.so'].y1f
y1f.restype = c_float
y1f.argtypes = [c_float]
y1l = _libraries['/usr/local/lib/libavcodec.so'].y1l
y1l.restype = c_longdouble
y1l.argtypes = [c_longdouble]
y1 = _libraries['/usr/local/lib/libavcodec.so'].y1
y1.restype = c_double
y1.argtypes = [c_double]
ynf = _libraries['/usr/local/lib/libavcodec.so'].ynf
ynf.restype = c_float
ynf.argtypes = [c_int, c_float]
ynl = _libraries['/usr/local/lib/libavcodec.so'].ynl
ynl.restype = c_longdouble
ynl.argtypes = [c_int, c_longdouble]
yn = _libraries['/usr/local/lib/libavcodec.so'].yn
yn.restype = c_double
yn.argtypes = [c_int, c_double]
erff = _libraries['/usr/local/lib/libavcodec.so'].erff
erff.restype = c_float
erff.argtypes = [c_float]
erf = _libraries['/usr/local/lib/libavcodec.so'].erf
erf.restype = c_double
erf.argtypes = [c_double]
erfl = _libraries['/usr/local/lib/libavcodec.so'].erfl
erfl.restype = c_longdouble
erfl.argtypes = [c_longdouble]
erfc = _libraries['/usr/local/lib/libavcodec.so'].erfc
erfc.restype = c_double
erfc.argtypes = [c_double]
erfcf = _libraries['/usr/local/lib/libavcodec.so'].erfcf
erfcf.restype = c_float
erfcf.argtypes = [c_float]
erfcl = _libraries['/usr/local/lib/libavcodec.so'].erfcl
erfcl.restype = c_longdouble
erfcl.argtypes = [c_longdouble]
lgammaf = _libraries['/usr/local/lib/libavcodec.so'].lgammaf
lgammaf.restype = c_float
lgammaf.argtypes = [c_float]
lgammal = _libraries['/usr/local/lib/libavcodec.so'].lgammal
lgammal.restype = c_longdouble
lgammal.argtypes = [c_longdouble]
lgamma = _libraries['/usr/local/lib/libavcodec.so'].lgamma
lgamma.restype = c_double
lgamma.argtypes = [c_double]
tgammaf = _libraries['/usr/local/lib/libavcodec.so'].tgammaf
tgammaf.restype = c_float
tgammaf.argtypes = [c_float]
tgammal = _libraries['/usr/local/lib/libavcodec.so'].tgammal
tgammal.restype = c_longdouble
tgammal.argtypes = [c_longdouble]
tgamma = _libraries['/usr/local/lib/libavcodec.so'].tgamma
tgamma.restype = c_double
tgamma.argtypes = [c_double]
gamma = _libraries['/usr/local/lib/libavcodec.so'].gamma
gamma.restype = c_double
gamma.argtypes = [c_double]
gammaf = _libraries['/usr/local/lib/libavcodec.so'].gammaf
gammaf.restype = c_float
gammaf.argtypes = [c_float]
gammal = _libraries['/usr/local/lib/libavcodec.so'].gammal
gammal.restype = c_longdouble
gammal.argtypes = [c_longdouble]
lgammal_r = _libraries['/usr/local/lib/libavcodec.so'].lgammal_r
lgammal_r.restype = c_longdouble
lgammal_r.argtypes = [c_longdouble, POINTER(c_int)]
lgammaf_r = _libraries['/usr/local/lib/libavcodec.so'].lgammaf_r
lgammaf_r.restype = c_float
lgammaf_r.argtypes = [c_float, POINTER(c_int)]
lgamma_r = _libraries['/usr/local/lib/libavcodec.so'].lgamma_r
lgamma_r.restype = c_double
lgamma_r.argtypes = [c_double, POINTER(c_int)]
rintl = _libraries['/usr/local/lib/libavcodec.so'].rintl
rintl.restype = c_longdouble
rintl.argtypes = [c_longdouble]
rintf = _libraries['/usr/local/lib/libavcodec.so'].rintf
rintf.restype = c_float
rintf.argtypes = [c_float]
rint = _libraries['/usr/local/lib/libavcodec.so'].rint
rint.restype = c_double
rint.argtypes = [c_double]
nextafterf = _libraries['/usr/local/lib/libavcodec.so'].nextafterf
nextafterf.restype = c_float
nextafterf.argtypes = [c_float, c_float]
nextafterl = _libraries['/usr/local/lib/libavcodec.so'].nextafterl
nextafterl.restype = c_longdouble
nextafterl.argtypes = [c_longdouble, c_longdouble]
nextafter = _libraries['/usr/local/lib/libavcodec.so'].nextafter
nextafter.restype = c_double
nextafter.argtypes = [c_double, c_double]
nexttoward = _libraries['/usr/local/lib/libavcodec.so'].nexttoward
nexttoward.restype = c_double
nexttoward.argtypes = [c_double, c_longdouble]
nexttowardf = _libraries['/usr/local/lib/libavcodec.so'].nexttowardf
nexttowardf.restype = c_float
nexttowardf.argtypes = [c_float, c_longdouble]
nexttowardl = _libraries['/usr/local/lib/libavcodec.so'].nexttowardl
nexttowardl.restype = c_longdouble
nexttowardl.argtypes = [c_longdouble, c_longdouble]
remainder = _libraries['/usr/local/lib/libavcodec.so'].remainder
remainder.restype = c_double
remainder.argtypes = [c_double, c_double]
remainderl = _libraries['/usr/local/lib/libavcodec.so'].remainderl
remainderl.restype = c_longdouble
remainderl.argtypes = [c_longdouble, c_longdouble]
remainderf = _libraries['/usr/local/lib/libavcodec.so'].remainderf
remainderf.restype = c_float
remainderf.argtypes = [c_float, c_float]
scalbnf = _libraries['/usr/local/lib/libavcodec.so'].scalbnf
scalbnf.restype = c_float
scalbnf.argtypes = [c_float, c_int]
scalbnl = _libraries['/usr/local/lib/libavcodec.so'].scalbnl
scalbnl.restype = c_longdouble
scalbnl.argtypes = [c_longdouble, c_int]
scalbn = _libraries['/usr/local/lib/libavcodec.so'].scalbn
scalbn.restype = c_double
scalbn.argtypes = [c_double, c_int]
ilogbl = _libraries['/usr/local/lib/libavcodec.so'].ilogbl
ilogbl.restype = c_int
ilogbl.argtypes = [c_longdouble]
ilogbf = _libraries['/usr/local/lib/libavcodec.so'].ilogbf
ilogbf.restype = c_int
ilogbf.argtypes = [c_float]
ilogb = _libraries['/usr/local/lib/libavcodec.so'].ilogb
ilogb.restype = c_int
ilogb.argtypes = [c_double]
scalblnf = _libraries['/usr/local/lib/libavcodec.so'].scalblnf
scalblnf.restype = c_float
scalblnf.argtypes = [c_float, c_long]
scalblnl = _libraries['/usr/local/lib/libavcodec.so'].scalblnl
scalblnl.restype = c_longdouble
scalblnl.argtypes = [c_longdouble, c_long]
scalbln = _libraries['/usr/local/lib/libavcodec.so'].scalbln
scalbln.restype = c_double
scalbln.argtypes = [c_double, c_long]
nearbyintl = _libraries['/usr/local/lib/libavcodec.so'].nearbyintl
nearbyintl.restype = c_longdouble
nearbyintl.argtypes = [c_longdouble]
nearbyint = _libraries['/usr/local/lib/libavcodec.so'].nearbyint
nearbyint.restype = c_double
nearbyint.argtypes = [c_double]
nearbyintf = _libraries['/usr/local/lib/libavcodec.so'].nearbyintf
nearbyintf.restype = c_float
nearbyintf.argtypes = [c_float]
round = _libraries['/usr/local/lib/libavcodec.so'].round
round.restype = c_double
round.argtypes = [c_double]
roundf = _libraries['/usr/local/lib/libavcodec.so'].roundf
roundf.restype = c_float
roundf.argtypes = [c_float]
roundl = _libraries['/usr/local/lib/libavcodec.so'].roundl
roundl.restype = c_longdouble
roundl.argtypes = [c_longdouble]
truncf = _libraries['/usr/local/lib/libavcodec.so'].truncf
truncf.restype = c_float
truncf.argtypes = [c_float]
truncl = _libraries['/usr/local/lib/libavcodec.so'].truncl
truncl.restype = c_longdouble
truncl.argtypes = [c_longdouble]
trunc = _libraries['/usr/local/lib/libavcodec.so'].trunc
trunc.restype = c_double
trunc.argtypes = [c_double]
remquo = _libraries['/usr/local/lib/libavcodec.so'].remquo
remquo.restype = c_double
remquo.argtypes = [c_double, c_double, POINTER(c_int)]
remquof = _libraries['/usr/local/lib/libavcodec.so'].remquof
remquof.restype = c_float
remquof.argtypes = [c_float, c_float, POINTER(c_int)]
remquol = _libraries['/usr/local/lib/libavcodec.so'].remquol
remquol.restype = c_longdouble
remquol.argtypes = [c_longdouble, c_longdouble, POINTER(c_int)]
lrintf = _libraries['/usr/local/lib/libavcodec.so'].lrintf
lrintf.restype = c_long
lrintf.argtypes = [c_float]
lrintl = _libraries['/usr/local/lib/libavcodec.so'].lrintl
lrintl.restype = c_long
lrintl.argtypes = [c_longdouble]
lrint = _libraries['/usr/local/lib/libavcodec.so'].lrint
lrint.restype = c_long
lrint.argtypes = [c_double]
llrintf = _libraries['/usr/local/lib/libavcodec.so'].llrintf
llrintf.restype = c_longlong
llrintf.argtypes = [c_float]
llrintl = _libraries['/usr/local/lib/libavcodec.so'].llrintl
llrintl.restype = c_longlong
llrintl.argtypes = [c_longdouble]
llrint = _libraries['/usr/local/lib/libavcodec.so'].llrint
llrint.restype = c_longlong
llrint.argtypes = [c_double]
lroundf = _libraries['/usr/local/lib/libavcodec.so'].lroundf
lroundf.restype = c_long
lroundf.argtypes = [c_float]
lroundl = _libraries['/usr/local/lib/libavcodec.so'].lroundl
lroundl.restype = c_long
lroundl.argtypes = [c_longdouble]
lround = _libraries['/usr/local/lib/libavcodec.so'].lround
lround.restype = c_long
lround.argtypes = [c_double]
llroundf = _libraries['/usr/local/lib/libavcodec.so'].llroundf
llroundf.restype = c_longlong
llroundf.argtypes = [c_float]
llround = _libraries['/usr/local/lib/libavcodec.so'].llround
llround.restype = c_longlong
llround.argtypes = [c_double]
llroundl = _libraries['/usr/local/lib/libavcodec.so'].llroundl
llroundl.restype = c_longlong
llroundl.argtypes = [c_longdouble]
fdim = _libraries['/usr/local/lib/libavcodec.so'].fdim
fdim.restype = c_double
fdim.argtypes = [c_double, c_double]
fdimf = _libraries['/usr/local/lib/libavcodec.so'].fdimf
fdimf.restype = c_float
fdimf.argtypes = [c_float, c_float]
fdiml = _libraries['/usr/local/lib/libavcodec.so'].fdiml
fdiml.restype = c_longdouble
fdiml.argtypes = [c_longdouble, c_longdouble]
fmax = _libraries['/usr/local/lib/libavcodec.so'].fmax
fmax.restype = c_double
fmax.argtypes = [c_double, c_double]
fmaxl = _libraries['/usr/local/lib/libavcodec.so'].fmaxl
fmaxl.restype = c_longdouble
fmaxl.argtypes = [c_longdouble, c_longdouble]
fmaxf = _libraries['/usr/local/lib/libavcodec.so'].fmaxf
fmaxf.restype = c_float
fmaxf.argtypes = [c_float, c_float]
fmin = _libraries['/usr/local/lib/libavcodec.so'].fmin
fmin.restype = c_double
fmin.argtypes = [c_double, c_double]
fminl = _libraries['/usr/local/lib/libavcodec.so'].fminl
fminl.restype = c_longdouble
fminl.argtypes = [c_longdouble, c_longdouble]
fminf = _libraries['/usr/local/lib/libavcodec.so'].fminf
fminf.restype = c_float
fminf.argtypes = [c_float, c_float]
__fpclassify = _libraries['/usr/local/lib/libavcodec.so'].__fpclassify
__fpclassify.restype = c_int
__fpclassify.argtypes = [c_double]
__fpclassifyl = _libraries['/usr/local/lib/libavcodec.so'].__fpclassifyl
__fpclassifyl.restype = c_int
__fpclassifyl.argtypes = [c_longdouble]
__fpclassifyf = _libraries['/usr/local/lib/libavcodec.so'].__fpclassifyf
__fpclassifyf.restype = c_int
__fpclassifyf.argtypes = [c_float]
fmal = _libraries['/usr/local/lib/libavcodec.so'].fmal
fmal.restype = c_longdouble
fmal.argtypes = [c_longdouble, c_longdouble, c_longdouble]
fma = _libraries['/usr/local/lib/libavcodec.so'].fma
fma.restype = c_double
fma.argtypes = [c_double, c_double, c_double]
fmaf = _libraries['/usr/local/lib/libavcodec.so'].fmaf
fmaf.restype = c_float
fmaf.argtypes = [c_float, c_float, c_float]
scalbf = _libraries['/usr/local/lib/libavcodec.so'].scalbf
scalbf.restype = c_float
scalbf.argtypes = [c_float, c_float]
scalbl = _libraries['/usr/local/lib/libavcodec.so'].scalbl
scalbl.restype = c_longdouble
scalbl.argtypes = [c_longdouble, c_longdouble]
scalb = _libraries['/usr/local/lib/libavcodec.so'].scalb
scalb.restype = c_double
scalb.argtypes = [c_double, c_double]
float_t = c_float
double_t = c_double
__signbitf = _libraries['/usr/local/lib/libavcodec.so'].__signbitf
__signbitf.restype = c_int
__signbitf.argtypes = [c_float]
__signbit = _libraries['/usr/local/lib/libavcodec.so'].__signbit
__signbit.restype = c_int
__signbit.argtypes = [c_double]
__signbitl = _libraries['/usr/local/lib/libavcodec.so'].__signbitl
__signbitl.restype = c_int
__signbitl.argtypes = [c_longdouble]
pthread_t = c_ulong
class pthread_attr_t(Union):
    pass
pthread_attr_t._fields_ = [
    ('__size', c_char * 56),
    ('__align', c_long),
]
class __pthread_internal_list(Structure):
    pass
__pthread_internal_list._fields_ = [
    ('__prev', POINTER(__pthread_internal_list)),
    ('__next', POINTER(__pthread_internal_list)),
]
__pthread_list_t = __pthread_internal_list
class __pthread_mutex_s(Structure):
    pass
__pthread_mutex_s._fields_ = [
    ('__lock', c_int),
    ('__count', c_uint),
    ('__owner', c_int),
    ('__nusers', c_uint),
    ('__kind', c_int),
    ('__spins', c_int),
    ('__list', __pthread_list_t),
]
class pthread_mutex_t(Union):
    pass
pthread_mutex_t._fields_ = [
    ('__data', __pthread_mutex_s),
    ('__size', c_char * 40),
    ('__align', c_long),
]
class pthread_mutexattr_t(Union):
    pass
pthread_mutexattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
class N14pthread_cond_t4DOT_22E(Structure):
    pass
N14pthread_cond_t4DOT_22E._fields_ = [
    ('__lock', c_int),
    ('__futex', c_uint),
    ('__total_seq', c_ulonglong),
    ('__wakeup_seq', c_ulonglong),
    ('__woken_seq', c_ulonglong),
    ('__mutex', c_void_p),
    ('__nwaiters', c_uint),
    ('__broadcast_seq', c_uint),
]
class pthread_cond_t(Union):
    pass
pthread_cond_t._fields_ = [
    ('__data', N14pthread_cond_t4DOT_22E),
    ('__size', c_char * 48),
    ('__align', c_longlong),
]
class pthread_condattr_t(Union):
    pass
pthread_condattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
pthread_key_t = c_uint
pthread_once_t = c_int
class N16pthread_rwlock_t4DOT_25E(Structure):
    pass
N16pthread_rwlock_t4DOT_25E._fields_ = [
    ('__lock', c_int),
    ('__nr_readers', c_uint),
    ('__readers_wakeup', c_uint),
    ('__writer_wakeup', c_uint),
    ('__nr_readers_queued', c_uint),
    ('__nr_writers_queued', c_uint),
    ('__writer', c_int),
    ('__shared', c_int),
    ('__pad1', c_ulong),
    ('__pad2', c_ulong),
    ('__flags', c_uint),
]
class pthread_rwlock_t(Union):
    pass
pthread_rwlock_t._fields_ = [
    ('__data', N16pthread_rwlock_t4DOT_25E),
    ('__size', c_char * 56),
    ('__align', c_long),
]
class pthread_rwlockattr_t(Union):
    pass
pthread_rwlockattr_t._fields_ = [
    ('__size', c_char * 8),
    ('__align', c_long),
]
pthread_spinlock_t = c_int
class pthread_barrier_t(Union):
    pass
pthread_barrier_t._fields_ = [
    ('__size', c_char * 32),
    ('__align', c_long),
]
class pthread_barrierattr_t(Union):
    pass
pthread_barrierattr_t._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]
__sig_atomic_t = c_int
class __sigset_t(Structure):
    pass
__sigset_t._fields_ = [
    ('__val', c_ulong * 16),
]
getchar = _libraries['/usr/local/lib/libavcodec.so'].getchar
getchar.restype = c_int
getchar.argtypes = []
fgetc_unlocked = _libraries['/usr/local/lib/libavcodec.so'].fgetc_unlocked
fgetc_unlocked.restype = c_int
fgetc_unlocked.argtypes = [POINTER(FILE)]
getc_unlocked = _libraries['/usr/local/lib/libavcodec.so'].getc_unlocked
getc_unlocked.restype = c_int
getc_unlocked.argtypes = [POINTER(FILE)]
getchar_unlocked = _libraries['/usr/local/lib/libavcodec.so'].getchar_unlocked
getchar_unlocked.restype = c_int
getchar_unlocked.argtypes = []
putchar = _libraries['/usr/local/lib/libavcodec.so'].putchar
putchar.restype = c_int
putchar.argtypes = [c_int]
fputc_unlocked = _libraries['/usr/local/lib/libavcodec.so'].fputc_unlocked
fputc_unlocked.restype = c_int
fputc_unlocked.argtypes = [c_int, POINTER(FILE)]
putc_unlocked = _libraries['/usr/local/lib/libavcodec.so'].putc_unlocked
putc_unlocked.restype = c_int
putc_unlocked.argtypes = [c_int, POINTER(FILE)]
putchar_unlocked = _libraries['/usr/local/lib/libavcodec.so'].putchar_unlocked
putchar_unlocked.restype = c_int
putchar_unlocked.argtypes = [c_int]
getline = _libraries['/usr/local/lib/libavcodec.so'].getline
getline.restype = __ssize_t
getline.argtypes = [POINTER(STRING), POINTER(size_t), POINTER(FILE)]
feof_unlocked = _libraries['/usr/local/lib/libavcodec.so'].feof_unlocked
feof_unlocked.restype = c_int
feof_unlocked.argtypes = [POINTER(FILE)]
ferror_unlocked = _libraries['/usr/local/lib/libavcodec.so'].ferror_unlocked
ferror_unlocked.restype = c_int
ferror_unlocked.argtypes = [POINTER(FILE)]
__sprintf_chk = _libraries['/usr/local/lib/libavcodec.so'].__sprintf_chk
__sprintf_chk.restype = c_int
__sprintf_chk.argtypes = [STRING, c_int, size_t, STRING]
__vsprintf_chk = _libraries['/usr/local/lib/libavcodec.so'].__vsprintf_chk
__vsprintf_chk.restype = c_int
__vsprintf_chk.argtypes = [STRING, c_int, size_t, STRING, POINTER(__va_list_tag)]
sprintf = _libraries['/usr/local/lib/libavcodec.so'].sprintf
sprintf.restype = c_int
sprintf.argtypes = [STRING, STRING]
vsprintf = _libraries['/usr/local/lib/libavcodec.so'].vsprintf
vsprintf.restype = c_int
vsprintf.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
__snprintf_chk = _libraries['/usr/local/lib/libavcodec.so'].__snprintf_chk
__snprintf_chk.restype = c_int
__snprintf_chk.argtypes = [STRING, size_t, c_int, size_t, STRING]
__vsnprintf_chk = _libraries['/usr/local/lib/libavcodec.so'].__vsnprintf_chk
__vsnprintf_chk.restype = c_int
__vsnprintf_chk.argtypes = [STRING, size_t, c_int, size_t, STRING, POINTER(__va_list_tag)]
snprintf = _libraries['/usr/local/lib/libavcodec.so'].snprintf
snprintf.restype = c_int
snprintf.argtypes = [STRING, size_t, STRING]
vsnprintf = _libraries['/usr/local/lib/libavcodec.so'].vsnprintf
vsnprintf.restype = c_int
vsnprintf.argtypes = [STRING, size_t, STRING, POINTER(__va_list_tag)]
__fprintf_chk = _libraries['/usr/local/lib/libavcodec.so'].__fprintf_chk
__fprintf_chk.restype = c_int
__fprintf_chk.argtypes = [POINTER(FILE), c_int, STRING]
__printf_chk = _libraries['/usr/local/lib/libavcodec.so'].__printf_chk
__printf_chk.restype = c_int
__printf_chk.argtypes = [c_int, STRING]
__vfprintf_chk = _libraries['/usr/local/lib/libavcodec.so'].__vfprintf_chk
__vfprintf_chk.restype = c_int
__vfprintf_chk.argtypes = [POINTER(FILE), c_int, STRING, POINTER(__va_list_tag)]
__vprintf_chk = _libraries['/usr/local/lib/libavcodec.so'].__vprintf_chk
__vprintf_chk.restype = c_int
__vprintf_chk.argtypes = [c_int, STRING, POINTER(__va_list_tag)]
fprintf = _libraries['/usr/local/lib/libavcodec.so'].fprintf
fprintf.restype = c_int
fprintf.argtypes = [POINTER(FILE), STRING]
printf = _libraries['/usr/local/lib/libavcodec.so'].printf
printf.restype = c_int
printf.argtypes = [STRING]
vprintf = _libraries['/usr/local/lib/libavcodec.so'].vprintf
vprintf.restype = c_int
vprintf.argtypes = [STRING, POINTER(__va_list_tag)]
vfprintf = _libraries['/usr/local/lib/libavcodec.so'].vfprintf
vfprintf.restype = c_int
vfprintf.argtypes = [POINTER(FILE), STRING, POINTER(__va_list_tag)]
__asprintf_chk = _libraries['/usr/local/lib/libavcodec.so'].__asprintf_chk
__asprintf_chk.restype = c_int
__asprintf_chk.argtypes = [POINTER(STRING), c_int, STRING]
__vasprintf_chk = _libraries['/usr/local/lib/libavcodec.so'].__vasprintf_chk
__vasprintf_chk.restype = c_int
__vasprintf_chk.argtypes = [POINTER(STRING), c_int, STRING, POINTER(__va_list_tag)]
__dprintf_chk = _libraries['/usr/local/lib/libavcodec.so'].__dprintf_chk
__dprintf_chk.restype = c_int
__dprintf_chk.argtypes = [c_int, c_int, STRING]
__vdprintf_chk = _libraries['/usr/local/lib/libavcodec.so'].__vdprintf_chk
__vdprintf_chk.restype = c_int
__vdprintf_chk.argtypes = [c_int, c_int, STRING, POINTER(__va_list_tag)]
__obstack_printf_chk = _libraries['/usr/local/lib/libavcodec.so'].__obstack_printf_chk
__obstack_printf_chk.restype = c_int
__obstack_printf_chk.argtypes = [POINTER(obstack), c_int, STRING]
__obstack_vprintf_chk = _libraries['/usr/local/lib/libavcodec.so'].__obstack_vprintf_chk
__obstack_vprintf_chk.restype = c_int
__obstack_vprintf_chk.argtypes = [POINTER(obstack), c_int, STRING, POINTER(__va_list_tag)]
asprintf = _libraries['/usr/local/lib/libavcodec.so'].asprintf
asprintf.restype = c_int
asprintf.argtypes = [POINTER(STRING), STRING]
__asprintf = _libraries['/usr/local/lib/libavcodec.so'].__asprintf
__asprintf.restype = c_int
__asprintf.argtypes = [POINTER(STRING), STRING]
dprintf = _libraries['/usr/local/lib/libavcodec.so'].dprintf
dprintf.restype = c_int
dprintf.argtypes = [c_int, STRING]
obstack_printf = _libraries['/usr/local/lib/libavcodec.so'].obstack_printf
obstack_printf.restype = c_int
obstack_printf.argtypes = [POINTER(obstack), STRING]
vasprintf = _libraries['/usr/local/lib/libavcodec.so'].vasprintf
vasprintf.restype = c_int
vasprintf.argtypes = [POINTER(STRING), STRING, POINTER(__va_list_tag)]
vdprintf = _libraries['/usr/local/lib/libavcodec.so'].vdprintf
vdprintf.restype = c_int
vdprintf.argtypes = [c_int, STRING, POINTER(__va_list_tag)]
obstack_vprintf = _libraries['/usr/local/lib/libavcodec.so'].obstack_vprintf
obstack_vprintf.restype = c_int
obstack_vprintf.argtypes = [POINTER(obstack), STRING, POINTER(__va_list_tag)]
__gets_chk = _libraries['/usr/local/lib/libavcodec.so'].__gets_chk
__gets_chk.restype = STRING
__gets_chk.argtypes = [STRING, size_t]
gets = _libraries['/usr/local/lib/libavcodec.so'].gets
gets.restype = STRING
gets.argtypes = [STRING]
__fgets_chk = _libraries['/usr/local/lib/libavcodec.so'].__fgets_chk
__fgets_chk.restype = STRING
__fgets_chk.argtypes = [STRING, size_t, c_int, POINTER(FILE)]
fgets = _libraries['/usr/local/lib/libavcodec.so'].fgets
fgets.restype = STRING
fgets.argtypes = [STRING, c_int, POINTER(FILE)]
__fread_chk = _libraries['/usr/local/lib/libavcodec.so'].__fread_chk
__fread_chk.restype = size_t
__fread_chk.argtypes = [c_void_p, size_t, size_t, size_t, POINTER(FILE)]
fread = _libraries['/usr/local/lib/libavcodec.so'].fread
fread.restype = size_t
fread.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
__fgets_unlocked_chk = _libraries['/usr/local/lib/libavcodec.so'].__fgets_unlocked_chk
__fgets_unlocked_chk.restype = STRING
__fgets_unlocked_chk.argtypes = [STRING, size_t, c_int, POINTER(FILE)]
fgets_unlocked = _libraries['/usr/local/lib/libavcodec.so'].fgets_unlocked
fgets_unlocked.restype = STRING
fgets_unlocked.argtypes = [STRING, c_int, POINTER(FILE)]
__fread_unlocked_chk = _libraries['/usr/local/lib/libavcodec.so'].__fread_unlocked_chk
__fread_unlocked_chk.restype = size_t
__fread_unlocked_chk.argtypes = [c_void_p, size_t, size_t, size_t, POINTER(FILE)]
fread_unlocked = _libraries['/usr/local/lib/libavcodec.so'].fread_unlocked
fread_unlocked.restype = size_t
fread_unlocked.argtypes = [c_void_p, size_t, size_t, POINTER(FILE)]
__realpath_chk = _libraries['/usr/local/lib/libavcodec.so'].__realpath_chk
__realpath_chk.restype = STRING
__realpath_chk.argtypes = [STRING, STRING, size_t]
realpath = _libraries['/usr/local/lib/libavcodec.so'].realpath
realpath.restype = STRING
realpath.argtypes = [STRING, STRING]
__ptsname_r_chk = _libraries['/usr/local/lib/libavcodec.so'].__ptsname_r_chk
__ptsname_r_chk.restype = c_int
__ptsname_r_chk.argtypes = [c_int, STRING, size_t, size_t]
ptsname_r = _libraries['/usr/local/lib/libavcodec.so'].ptsname_r
ptsname_r.restype = c_int
ptsname_r.argtypes = [c_int, STRING, size_t]
__wctomb_chk = _libraries['/usr/local/lib/libavcodec.so'].__wctomb_chk
__wctomb_chk.restype = c_int
__wctomb_chk.argtypes = [STRING, c_wchar, size_t]
wctomb = _libraries['/usr/local/lib/libavcodec.so'].wctomb
wctomb.restype = c_int
wctomb.argtypes = [STRING, c_wchar]
__mbstowcs_chk = _libraries['/usr/local/lib/libavcodec.so'].__mbstowcs_chk
__mbstowcs_chk.restype = size_t
__mbstowcs_chk.argtypes = [WSTRING, STRING, size_t, size_t]
mbstowcs = _libraries['/usr/local/lib/libavcodec.so'].mbstowcs
mbstowcs.restype = size_t
mbstowcs.argtypes = [WSTRING, STRING, size_t]
__wcstombs_chk = _libraries['/usr/local/lib/libavcodec.so'].__wcstombs_chk
__wcstombs_chk.restype = size_t
__wcstombs_chk.argtypes = [STRING, WSTRING, size_t, size_t]
wcstombs = _libraries['/usr/local/lib/libavcodec.so'].wcstombs
wcstombs.restype = size_t
wcstombs.argtypes = [STRING, WSTRING, size_t]
memcpy = _libraries['/usr/local/lib/libavcodec.so'].memcpy
memcpy.restype = c_void_p
memcpy.argtypes = [c_void_p, c_void_p, size_t]
memmove = _libraries['/usr/local/lib/libavcodec.so'].memmove
memmove.restype = c_void_p
memmove.argtypes = [c_void_p, c_void_p, size_t]
mempcpy = _libraries['/usr/local/lib/libavcodec.so'].mempcpy
mempcpy.restype = c_void_p
mempcpy.argtypes = [c_void_p, c_void_p, size_t]
memset = _libraries['/usr/local/lib/libavcodec.so'].memset
memset.restype = c_void_p
memset.argtypes = [c_void_p, c_int, size_t]
bcopy = _libraries['/usr/local/lib/libavcodec.so'].bcopy
bcopy.restype = None
bcopy.argtypes = [c_void_p, c_void_p, size_t]
bzero = _libraries['/usr/local/lib/libavcodec.so'].bzero
bzero.restype = None
bzero.argtypes = [c_void_p, size_t]
strcpy = _libraries['/usr/local/lib/libavcodec.so'].strcpy
strcpy.restype = STRING
strcpy.argtypes = [STRING, STRING]
stpcpy = _libraries['/usr/local/lib/libavcodec.so'].stpcpy
stpcpy.restype = STRING
stpcpy.argtypes = [STRING, STRING]
strncpy = _libraries['/usr/local/lib/libavcodec.so'].strncpy
strncpy.restype = STRING
strncpy.argtypes = [STRING, STRING, size_t]
__stpncpy_chk = _libraries['/usr/local/lib/libavcodec.so'].__stpncpy_chk
__stpncpy_chk.restype = STRING
__stpncpy_chk.argtypes = [STRING, STRING, size_t, size_t]
stpncpy = _libraries['/usr/local/lib/libavcodec.so'].stpncpy
stpncpy.restype = STRING
stpncpy.argtypes = [STRING, STRING, size_t]
strcat = _libraries['/usr/local/lib/libavcodec.so'].strcat
strcat.restype = STRING
strcat.argtypes = [STRING, STRING]
strncat = _libraries['/usr/local/lib/libavcodec.so'].strncat
strncat.restype = STRING
strncat.argtypes = [STRING, STRING, size_t]
sys_nerr = (c_int).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'sys_nerr')
sys_errlist = (STRING * 0).in_dll(_libraries['/usr/local/lib/libavcodec.so'], 'sys_errlist')
_sys_nerr = (c_int).in_dll(_libraries['/usr/local/lib/libavcodec.so'], '_sys_nerr')
_sys_errlist = (STRING * 0).in_dll(_libraries['/usr/local/lib/libavcodec.so'], '_sys_errlist')
class timeval(Structure):
    pass
__suseconds_t = c_long
timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]
__u_char = c_ubyte
__u_short = c_ushort
__u_int = c_uint
__u_long = c_ulong
__int8_t = c_byte
__uint8_t = c_ubyte
__int16_t = c_short
__uint16_t = c_ushort
__uint32_t = c_uint
__int64_t = c_long
__uint64_t = c_ulong
__quad_t = c_long
__u_quad_t = c_ulong
__dev_t = c_ulong
__gid_t = c_uint
__ino_t = c_ulong
__ino64_t = c_ulong
__mode_t = c_uint
__nlink_t = c_ulong
class __fsid_t(Structure):
    pass
__fsid_t._fields_ = [
    ('__val', c_int * 2),
]
__rlim_t = c_ulong
__rlim64_t = c_ulong
__id_t = c_uint
__useconds_t = c_uint
__daddr_t = c_int
__swblk_t = c_long
__key_t = c_int
__blksize_t = c_long
__blkcnt_t = c_long
__blkcnt64_t = c_long
__fsblkcnt_t = c_ulong
__fsblkcnt64_t = c_ulong
__fsfilcnt_t = c_ulong
__fsfilcnt64_t = c_ulong
__loff_t = __off64_t
__qaddr_t = POINTER(__quad_t)
__caddr_t = STRING
__intptr_t = c_long
__socklen_t = c_uint
class wait(Union):
    pass
class N4wait4DOT_11E(Structure):
    pass
N4wait4DOT_11E._fields_ = [
    ('__w_termsig', c_uint, 7),
    ('__w_coredump', c_uint, 1),
    ('__w_retcode', c_uint, 8),
    ('', c_uint, 16),
]
class N4wait4DOT_12E(Structure):
    pass
N4wait4DOT_12E._fields_ = [
    ('__w_stopval', c_uint, 8),
    ('__w_stopsig', c_uint, 8),
    ('', c_uint, 16),
]
wait._fields_ = [
    ('w_status', c_int),
    ('__wait_terminated', N4wait4DOT_11E),
    ('__wait_stopped', N4wait4DOT_12E),
]
sigset_t = __sigset_t
__fd_mask = c_long
class fd_set(Structure):
    pass
fd_set._fields_ = [
    ('fds_bits', __fd_mask * 16),
]
fd_mask = __fd_mask
select = _libraries['/usr/local/lib/libavcodec.so'].select
select.restype = c_int
select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timeval)]
pselect = _libraries['/usr/local/lib/libavcodec.so'].pselect
pselect.restype = c_int
pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timespec), POINTER(__sigset_t)]
gnu_dev_major = _libraries['/usr/local/lib/libavcodec.so'].gnu_dev_major
gnu_dev_major.restype = c_uint
gnu_dev_major.argtypes = [c_ulonglong]
gnu_dev_minor = _libraries['/usr/local/lib/libavcodec.so'].gnu_dev_minor
gnu_dev_minor.restype = c_uint
gnu_dev_minor.argtypes = [c_ulonglong]
gnu_dev_makedev = _libraries['/usr/local/lib/libavcodec.so'].gnu_dev_makedev
gnu_dev_makedev.restype = c_ulonglong
gnu_dev_makedev.argtypes = [c_uint, c_uint]
u_char = __u_char
u_short = __u_short
u_int = __u_int
u_long = __u_long
quad_t = __quad_t
u_quad_t = __u_quad_t
fsid_t = __fsid_t
loff_t = __loff_t
ino_t = __ino_t
ino64_t = __ino64_t
dev_t = __dev_t
gid_t = __gid_t
mode_t = __mode_t
nlink_t = __nlink_t
uid_t = __uid_t
id_t = __id_t
daddr_t = __daddr_t
caddr_t = __caddr_t
key_t = __key_t
useconds_t = __useconds_t
suseconds_t = __suseconds_t
ulong = c_ulong
ushort = c_ushort
uint = c_uint
u_int8_t = c_ubyte
u_int16_t = c_ushort
u_int32_t = c_uint
u_int64_t = c_ulong
register_t = c_long
blksize_t = __blksize_t
blkcnt_t = __blkcnt_t
fsblkcnt_t = __fsblkcnt_t
fsfilcnt_t = __fsfilcnt_t
blkcnt64_t = __blkcnt64_t
fsblkcnt64_t = __fsblkcnt64_t
fsfilcnt64_t = __fsfilcnt64_t
class __locale_data(Structure):
    pass
__locale_struct._fields_ = [
    ('__locales', POINTER(__locale_data) * 13),
    ('__ctype_b', POINTER(c_ushort)),
    ('__ctype_tolower', POINTER(c_int)),
    ('__ctype_toupper', POINTER(c_int)),
    ('__names', STRING * 13),
]
__locale_data._fields_ = [
]
locale_t = __locale_t
ptrdiff_t = c_long
__all__ = ['_ISlower', 'AVFMT_NOBINSEARCH', 'CODEC_ID_ADPCM_IMA_AMV',
           'ETXTBSY', 'math_errhandling', 'AV_ROUND_UP',
           'FF_CODER_TYPE_VLC', 'PP_CPU_CAPS_MMX', '__off64_t',
           'PIX_FMT_YUV422P', '__clockid_t_defined', 'timer_t',
           'PIX_FMT_YUVJ440P', 'AVMEDIA_TYPE_VIDEO',
           'avfilter_all_formats', 'FF_PROFILE_H264_HIGH_10',
           'EL3HLT', 'FILENAME_MAX', 'hypotf', 'ilogb',
           'AVClassCategory', 'AVPALETTE_COUNT',
           'AVFILTER_CMD_FLAG_FAST',
           'AV_DISPOSITION_HEARING_IMPAIRED', 'wctomb', '__FD_ISSET',
           '_IO_BUFSIZ', 'EFBIG', 'getpt', 'CODEC_ID_BINKVIDEO',
           'CODEC_ID_ASV2', '_IO_off64_t', 'CODEC_ID_ASV1',
           'AVSEEK_FLAG_BACKWARD', 'islessgreater', 'avfilter_link',
           'CLOCK_MONOTONIC_COARSE', 'AV_CLASS_CATEGORY_DEMUXER',
           'av_get_channel_layout_nb_channels', '__NFDBITS',
           'CODEC_ID_TIFF', 'FF_PROFILE_MPEG4_BASIC_ANIMATED_TEXTURE',
           'CODEC_ID_DIRAC', 'SWS_CS_DEFAULT',
           'av_get_picture_type_char', 'gnu_dev_makedev', 'FFALIGN',
           'avcodec_set_dimensions', '__va_list_tag', 'u_long',
           'AV_LOCK_CREATE', 'AV_CH_TOP_CENTER', 'SWS_CS_SMPTE240M',
           'SWS_CS_FCC', 'pp_free_context',
           'av_get_audio_frame_duration', '_POSIX_',
           '____gwchar_t_defined', 'avfilter_make_format_list',
           'AVCOL_PRI_FILM', 'av_packet_new_side_data',
           'FF_CMP_CHROMA', 'CODEC_ID_SMACKAUDIO',
           'AVCOL_TRC_UNSPECIFIED', 'WNOHANG', '_IO_SHOWBASE',
           'avcodec_encode_audio2', '__codecvt_partial', 'getdate_r',
           'WORD_BIT', 'PIX_FMT_RGB444BE', 'be64toh', 'copysign',
           'isctype', 'setstate_r', '__locale_data', 'CODEC_ID_PBM',
           'CODEC_ID_FFMETADATA', '__isgraph_l', 'AV_CH_LAYOUT_MONO',
           'FF_RC_STRATEGY_XVID', 'av_rescale', 'CODEC_FLAG_QPEL',
           'CODEC_CAP_AUTO_THREADS', 'AVDISCARD_NONE',
           'PIX_FMT_DXVA2_VLD', 'pthread_t', 'CODEC_ID_AASC',
           'sws_getConstVec', 'E2BIG', 'FF_PROFILE_MPEG4_MAIN',
           'ispunct_l', 'FF_LOSS_COLORQUANT', 'EHOSTDOWN',
           'AV_AUDIO_SERVICE_TYPE_NB', '_IO_DEC', 'EBUSY', 'qecvt',
           'printf', '_POSIX_STREAM_MAX', 'getchar', 'ENOTSOCK',
           'AV_CLASS_CATEGORY_MUXER', 'modff', 'fputs_unlocked',
           'isblank_l', 'LIBSWSCALE_IDENT', 'CODEC_ID_MICRODVD',
           'avio_wb16', 'AVMEDIA_TYPE_DATA', 'qecvt_r', 'ftello64',
           'FF_MB_DECISION_BITS', 'expm1', 'EDQUOT', '__iscntrl_l',
           'avio_get_str16le', 'avfilter_get_video_buffer',
           'LIBAVFORMAT_VERSION_MAJOR', '__WTERMSIG',
           'PIX_FMT_VDPAU_WMV3', 'M_PHI', 'strerror', 'AVBPrint',
           'CODEC_ID_WMV2', 'CODEC_ID_WMV3', 'CODEC_ID_WMV1',
           'avcodec_decode_audio4', 'AVFMT_VARIABLE_FPS',
           'avcodec_decode_audio3', '_POSIX_NGROUPS_MAX',
           '_IO_BOOLALPHA', 'EXFULL',
           'avfilter_set_common_pixel_formats', 'floor',
           'avcodec_alloc_frame', 'off_t', 'int_fast16_t',
           'PIX_FMT_VAAPI_MOCO', '__fpclassifyl',
           'CODEC_ID_PCM_S32LE', '__fsblkcnt_t', 'rand_r',
           'FF_CMP_SAD', 'avfilter_license', 'PIX_FMT_RGB48LE',
           '_POSIX2_EXPR_NEST_MAX', '__FILE', 'lrand48', 'memfrob',
           'ctime_r', '__WORDSIZE', 'CODEC_ID_MP3ON4',
           'CODEC_ID_PGMYUV', 'rewind', 'AVMediaType',
           'av_frame_set_channel_layout', 'AV_LOG_DEBUG',
           'CODEC_ID_PCM_S24LE', 'UINT32_C',
           'LIBAVDEVICE_VERSION_MICRO', 'FFUMOD', '_XOPEN_SOURCE',
           'avcodec_default_reget_buffer', 'CODEC_FLAG_PASS1',
           'PIX_FMT_BGR4_BYTE', 'PIX_FMT_UYVY422', 'valloc',
           '__GLIBC__', 'pthread_rwlockattr_t', 'CODEC_FLAG2_SKIP_RD',
           'AV_CH_LAYOUT_STEREO_DOWNMIX', '__secure_getenv',
           'funlockfile', 'strerror_r', 'avfilter_config_links',
           'getloadavg', '__u_int', 'SLICE_FLAG_ALLOW_PLANE',
           'avcodec_get_frame_class', 'avio_get_str16be',
           '_XLOCALE_H', 'CODEC_ID_PCM_F64BE', 'av_read_packet',
           'avfilter_null_get_video_buffer', 'PIX_FMT_MONOWHITE',
           'CODEC_CAP_SLICE_THREADS', 'strtouq', 'AVIndexEntry',
           '__time_t', 'ENOTTY', 'CODEC_CAP_FRAME_THREADS',
           'avcodec_decode_video2', 'strtoul', 'pthread_mutexattr_t',
           'finitel', 'AV_PICTURE_TYPE_BI', 'FF_IDCT_SIMPLEMMX',
           'ENOLINK', 'CODEC_ID_TRUEMOTION1', 'CODEC_ID_TRUEMOTION2',
           'AV_FIELD_BB', 'fwrite', 'EMLINK', 'MB_TYPE_INTRA4x4',
           'uint_least16_t', 'AVFMT_NOGENSEARCH', 'a64l', 'iscntrl',
           'FF_IDCT_SIMPLEARMV6', 'AV_FIELD_BT', 'AVCodecTag',
           'CODEC_ID_BMV_AUDIO', 'AIO_PRIO_DELTA_MAX', 'ECANCELED',
           'CODEC_ID_INDEO5', 'CODEC_ID_INDEO4', 'avio_skip',
           'CODEC_ID_INDEO2', 'u_char', 'FF_LAMBDA_SCALE', 'uid_t',
           'pow10f', 'AV_SAMPLE_FMT_S16P', 'u_int16_t', 'SWS_LANCZOS',
           'pow10l', 'AVFMT_NODIMENSIONS', 'FF_CMP_SSE',
           'av_get_frame_filename', 'AV_ROUND_ZERO', '_SYS_CDEFS_H',
           'AVSTREAM_PARSE_NONE', 'PIX_FMT_UYYVYY411',
           '__SIZEOF_PTHREAD_MUTEXATTR_T', 'CODEC_ID_IDF',
           'AVDISCARD_NONKEY', 'PTHREAD_STACK_MIN', 'FF_PRED_LEFT',
           'AVFMT_FLAG_NONBLOCK', 'CODEC_ID_IFF_ILBM', 'logb',
           'sinhf', 'fileno_unlocked', 'logl', 'sws_addVec',
           'WIFSIGNALED', 'av_parse_cpu_caps', 'av_find_stream_info',
           'uint_fast16_t', 'MB_TYPE_INTRA_PCM', 'uint_fast32_t',
           'SWS_PARAM_DEFAULT', 'div_t', 'ceill', 'sprintf', 'atol',
           'AVFMT_NOSTREAMS', 'CHARCLASS_NAME_MAX',
           'LIBSWSCALE_VERSION_MICRO', 'ELOOP', 'log2', 'strcspn',
           'AV_CPU_FLAG_SSSE3', 'PIX_FMT_GBRP10BE', 'lldiv_t',
           'tzname', 'MB_TYPE_INTERLACED',
           'av_frame_get_channel_layout', '__strtol_internal',
           'FF_CMP_ZERO', 'CODEC_ID_ZEROCODEC', 'CODEC_ID_MSZH',
           'AVFilterBuffer', 'htobe16', '__pthread_list_t',
           'av_find_program_from_stream', 'jrand48', 'isgraph',
           'erfc', 'AVERROR_PROTOCOL_NOT_FOUND', 'pow10',
           'CODEC_ID_4XM', 'erfl', 'CODEC_ID_SGI', 'scanf',
           'av_frame_get_pkt_pos', 'av_resample_compensate', 'floorf',
           '__suseconds_t', 'AV_DISPOSITION_FORCED',
           'clock_getcpuclockid', 'floorl', 'FF_MB_DECISION_RD',
           'ldexp', '_IO_lock_t', '_POSIX2_COLL_WEIGHTS_MAX',
           'CODEC_ID_ROQ', '__USE_ANSI', 'strncpy',
           'CODEC_ID_ATRAC3P', 'av_reduce', 'isalnum', '_sys_nerr',
           'exp2', 'av_get_profile_name', 'qsort', 'PIX_FMT_ARGB',
           'isalpha', 'ino64_t', 'memcmp', 'EISNAM', 'dprintf',
           'ecvt_r', 'FF_IDCT_SIMPLEVIS', 'y1l',
           'av_get_bits_per_sample_fmt', 'setbuffer',
           'av_append_packet', 'avio_flush', '__blkcnt64_t',
           'mkostemp', '__STDC_ISO_10646__', 'BC_DIM_MAX',
           '__vdprintf_chk', 'CODEC_ID_SUNRAST', 'avcodec_version',
           'N8AVStream4DOT_34E', 'CODEC_ID_CDXL',
           'CODEC_ID_ADPCM_EA_R3', '_BITS_TIME_H', '_IO_BE',
           'AV_AUDIO_SERVICE_TYPE_DIALOGUE', 'ULONG_MAX',
           'CODEC_ID_ADPCM_IMA_EA_EACS', 'expl', 'uint64_t', 'expf',
           '_IOS_INPUT', 'MB_TYPE_16x16', 'CODEC_ID_AC3',
           'CODEC_ID_ATRAC1', 'AVCHROMA_LOC_LEFT', 'avpicture_layout',
           'av_packet_merge_side_data', 'FF_PROFILE_UNKNOWN',
           'PDP_ENDIAN', 'SWS_BILINEAR', 'AVFMT_NO_BYTE_SEEK',
           '__rlim_t', '__FLOAT_WORD_ORDER', 'setstate', 'ENONET',
           'ECHRNG', 'FF_BUFFER_HINTS_READABLE', 'AV_EF_COMPLIANT',
           'AVCOL_TRC_GAMMA22', '__key_t', 'AVCOL_TRC_GAMMA28',
           'FF_CODER_TYPE_DEFLATE', 'avcodec_get_name',
           'FF_DEBUG_VIS_MV_B_FOR', 'CODEC_ID_MJPEG',
           'av_dynarray_add', 'SWS_CPU_CAPS_MMX', 'asin',
           'SWS_FAST_BILINEAR', '_IOS_ATEND', 'FF_BUG_HPEL_CHROMA',
           'PIX_FMT_YUV422P9BE', 'FF_CMP_DCT', 'HUGE_VALF',
           'LIBPOSTPROC_BUILD', 'FF_DEBUG_VIS_MV_B_BACK',
           '_POSIX_AIO_MAX', 'FF_QSCALE_TYPE_MPEG2',
           'MB_TYPE_DIRECT2', 'avcodec_get_context_defaults2',
           'CODEC_ID_RA_144', 'AVCOL_SPC_SMPTE170M',
           'AVERROR_FILTER_NOT_FOUND', 'AV_LOG_MAX_OFFSET',
           'LIBAVFILTER_VERSION_INT', 'AV_CH_LAYOUT_HEXAGONAL',
           'fseeko64', 'AVCOL_RANGE_NB', 'setlinebuf',
           'PIX_FMT_YUV422P10BE', 'setvbuf', 'EISDIR',
           'MAX_STD_TIMEBASES', 'av_log_set_level', 'AVSubtitle',
           'CODEC_ID_PCM_LXF', '__GNU_LIBRARY__', '_BITS_TYPESIZES_H',
           'nanf', 'AV_CH_FRONT_RIGHT_OF_CENTER',
           'av_bitstream_filter_close', '__underflow', 'INTMAX_C',
           'AV_SAMPLE_FMT_S32', '_IO_2_1_stdin_', '__fpclassify',
           'fgetpos64', 'AV_DISPOSITION_LYRICS', 'av_init_packet',
           'SWS_PRINT_INFO', 'AV_MATRIX_ENCODING_DPLII',
           'FF_BUG_OLD_MSMPEG4', 'llroundl', 'FF_PROFILE_DTS_ES',
           '_POSIX_RTSIG_MAX', 'av_frame_get_pkt_duration',
           '_POSIX_SEM_VALUE_MAX', 'lgammaf', 'AV_FIELD_UNKNOWN',
           'avio_rb64', 'AVColorPrimaries', 'lgammal', '_IO_LEFT',
           'UINT_MAX', 'ptsname_r', 'SWS_ACCURATE_RND', 'mkstemps64',
           'perror', 'srandom', '_tolower', 'gammal',
           'avcodec_register_all', 'PIX_FMT_GBR24P', 'dysize',
           'avcodec_string', 'PIX_FMT_YUV444P16BE',
           'PIX_FMT_VDPAU_MPEG4', '__fsid_t', 'strncmp',
           'av_get_exact_bits_per_sample', 'mkdtemp',
           'CODEC_ID_CINEPAK', 'CODEC_ID_FLASHSV', 'av_strerror',
           'avio_r8', 'sws_getIdentityVec', 'avcodec_default_execute',
           'AVProbeData', 'ENOTNAM', 'AVFieldOrder',
           'CODEC_CAP_HWACCEL_VDPAU', '_LIB_VERSION',
           'sws_freeFilter', 'fgetpos', '_IO_seekpos', 'SwsVector',
           'erfcf', 'posix_memalign', 'avfilter_free', 'CODEC_ID_GIF',
           'FP_INFINITE', '_POSIX_ARG_MAX', 'M_LOG2_10', '__overflow',
           'timelocal', '__FD_SETSIZE', 'FF_CMP_SATD',
           '__USE_XOPEN2K8', 'av_get_sample_fmt',
           'avfilter_start_frame', 'X_TLOSS', 'seed48_r',
           'AV_LOG_PANIC', 'N14pthread_cond_t4DOT_22E',
           '_IO_FILE_plus', 'AV_CH_LAYOUT_QUAD', 'AVDictionaryEntry',
           '_IO_va_list', 'avio_rl64', '__tzname', 'sws_scaleVec',
           'AV_SIDE_DATA_PARAM_CHANGE_SAMPLE_RATE', 'ldiv', 'drem',
           'CODEC_ID_A64_MULTI5', 'wcstoumax', 'AVCOL_PRI_SMPTE240M',
           'Motion_Est_ID', '__tolower_l', 'fabsf', 'EMFILE', 'fmaxf',
           'CODEC_ID_SRT', 'off64_t', 'fmaxl', 'fabsl', 'LONG_BIT',
           'AV_CH_LAYOUT_6POINT1', 'AV_CH_LAYOUT_6POINT0',
           'AV_PKT_DATA_NEW_EXTRADATA', 'CLOCK_MONOTONIC_RAW',
           'AV_PARSER_PTS_NB', 'htole64', 'av_nearer_q',
           '_POSIX_TTY_NAME_MAX', 'hypotl', '__finite',
           'CODEC_ID_PNG', 'gnu_dev_major', 'fminf', 'putc',
           'AV_CPU_FLAG_FMA4', 'trunc', 'AV_CPU_FLAG_SSE42',
           '_IO_HEX', 'fminl', 'FF_QP2LAMBDA', 'strsignal', 'j0l',
           'tmpnam', 'getdate_err', 'FF_PROFILE_H264_HIGH_10_INTRA',
           'MKTAG', '_IO_SKIPWS', '__WORDSIZE_COMPAT32',
           'avcodec_license', 'MB_TYPE_GMC',
           'av_get_packed_sample_fmt', 'av_frame_set_pkt_pos',
           'PIX_FMT_0RGB', 'EXIT_SUCCESS', 'AVBitStreamFilter',
           'CODEC_ID_DXA', 'tanh', 'tanf',
           'FF_PROFILE_MPEG4_SIMPLE_FACE_ANIMATION', 'av_dump_format',
           'CODEC_ID_V210', 'AVStreamParseType', 'CODEC_ID_VP6A',
           'FF_BUG_AC_VLC', 'clearenv', 'suseconds_t',
           'CODEC_ID_VP6F', 'avformat_open_input',
           'AV_CH_TOP_BACK_CENTER', 'ENOSTR', 'av_register_all',
           'av_parser_close', '__u_char', 'popen', 'exit',
           '_POSIX_SYMLOOP_MAX', 'AVFMT_FLAG_CUSTOM_IO',
           '_IO_SCIENTIFIC', 'CODEC_ID_MAD', 'avutil_version',
           'u_short', 'av_grow_packet', 'strnlen',
           'SWS_CPU_CAPS_SSE2', 'avio_wb32', '_IO_marker',
           'RTSIG_MAX', 'AV_CPU_FLAG_VFP', '_POSIX_HOST_NAME_MAX',
           'CODEC_ID_ZLIB', 'FF_DEBUG_VIS_MV_P_FOR',
           'PIX_FMT_BGR48LE', '__SIZEOF_PTHREAD_ATTR_T',
           'avcodec_configuration', 'PIX_FMT_PAL8',
           'CODEC_ID_DVD_SUBTITLE', '__ctype_tolower_loc',
           'av_new_packet', 'isinfl', '_IO_2_1_stdout_',
           '_POSIX_SIGQUEUE_MAX', 'LLONG_MIN', 'uint_fast64_t',
           'wcstombs', 'nrand48', 'pthread_mutex_t',
           'AVERROR_BSF_NOT_FOUND', 'CODEC_FLAG2_NO_OUTPUT',
           'LIBSWSCALE_VERSION_INT', 'FF_IDCT_CAVS',
           'CODEC_ID_JACOSUB', 'av_guess_sample_aspect_ratio',
           'AV_CPU_FLAG_VFPV3', 'CODEC_ID_VB', 'fseek',
           '__USE_XOPEN2KXSI', 'AVCOL_SPC_FCC',
           'CODEC_ID_IFF_BYTERUN1', 'AV_DICT_APPEND',
           'pthread_condattr_t', 'AVFMT_FLAG_NOFILLIN',
           'pthread_once_t', '__timer_t', 'AVFMT_ALLOW_FLUSH',
           'uint_least32_t', 'CODEC_ID_PCM_S32BE', 'isnormal',
           'PIX_FMT_VAAPI_IDCT', 'AV_LOG_VERBOSE', '__fprintf_chk',
           '_XOPEN_', 'CODEC_FLAG_LOOP_FILTER', 'RAND_MAX',
           'FF_LAMBDA_SHIFT', 'CODEC_ID_ADPCM_YAMAHA', 'PIX_FMT_NV12',
           'gnu_dev_minor', 'frexpl', 'loff_t', 'blksize_t',
           'CODEC_ID_G723_1', 'PIX_FMT_YUV440P', 'int_least32_t',
           'AVUNERROR', '__STDC_IEC_559__', 'CODEC_ID_VBLE',
           'av_log_set_callback', 'PIX_FMT_RGB565LE', 'dev_t',
           'FP_NORMAL', 'AVSEEK_FLAG_ANY', 'AVERROR_PATCHWELCOME',
           'AV_CH_FRONT_RIGHT', 'CODEC_ID_PCM_S24DAUD',
           'CODEC_ID_FIRST_SUBTITLE', 'ctime',
           'LIBPOSTPROC_VERSION_MICRO', 'PIX_FMT_RGB555LE',
           'CODEC_ID_QTRLE', 'float_t', 'AVCOL_SPC_SMPTE240M',
           'PIX_FMT_GRAY16BE', '_ISOC99_SOURCE', 'freopen',
           'PIX_FMT_YUV444P9BE', 'fread_unlocked',
           'AV_CH_STEREO_RIGHT', 'FF_PROFILE_H264_MAIN',
           'sws_freeContext', 'DOMAIN', 'ESRMNT', 'av_div_q',
           'rpmatch', 'CODEC_ID_MMVIDEO', 'FF_PROFILE_H264_HIGH',
           'CODEC_ID_DVAUDIO', 'CODEC_ID_WMAVOICE', 'QP_STORE_T',
           'AVFrac', 'ctermid', '__id_t', 'AV_HAVE_BIGENDIAN',
           '_IO_feof', 'CODEC_ID_MOTIONPIXELS', 'ESTALE',
           'AV_CH_TOP_FRONT_LEFT', '__timer_t_defined',
           'AV_CH_LAYOUT_6POINT1_FRONT', '_IO_FIXED',
           'LIBAVFILTER_VERSION_MAJOR', 'av_dbl2int',
           'av_probe_input_buffer', 'LIBAVUTIL_VERSION_INT',
           'FD_ISSET', 'gmtime', '__codecvt_result',
           '__vasprintf_chk', 'PIX_FMT_YUV444P9LE', 'fcloseall',
           'av_int2dbl', 'FF_IDCT_SIMPLENEON',
           'avformat_alloc_context', 'cbrtf', 'avio_enum_protocols',
           'FF_DEBUG_MV', 'MB_TYPE_P0L1', 'PIX_FMT_YUV420P16LE',
           'AVSampleFormat', 'lrintf', 'PIX_FMT_YUVA422P', 'acos',
           '_IO_IN_BACKUP', 'CODEC_ID_XAN_DPCM',
           'av_probe_input_format', 'tempnam', 'j1f',
           'FF_DTG_AFD_16_9', 'avcodec_get_chroma_sub_sample',
           'av_vlog', 'FF_ASPECT_EXTENDED',
           'AV_DISPOSITION_ATTACHED_PIC', 'sws_setColorspaceDetails',
           'getdelim', 'CODEC_ID_BINKAUDIO_DCT', 'CODEC_ID_MSVIDEO1',
           'CODEC_ID_BMV_VIDEO', 'avio_put_str',
           'sws_isSupportedOutput', 'CODEC_ID_PCM_U32BE',
           'CODEC_ID_WNV1', 'EKEYREJECTED', 'AVSEEK_FORCE',
           'FF_DEBUG_QP', 'avcodec_find_encoder', 'AVPacket',
           'ENOTCONN', 'AV_DICT_DONT_OVERWRITE', 'CODEC_ID_MDEC',
           'SWS_FULL_CHR_H_INP', 'SWS_FULL_CHR_H_INT', 'htobe32',
           'CODEC_ID_CELT', 'BUFSIZ', 'FF_BUG_AMV',
           '_POSIX_LOGIN_NAME_MAX', 'SwsContext', 'srand48',
           'PIX_FMT_RGB24', 'FF_PROFILE_MPEG2_MAIN', 'freopen64',
           'FF_DTG_AFD_4_3_SP_14_9', 'avio_open_dyn_buf',
           'avcodec_get_pix_fmt_loss', 'sws_getCoefficients',
           '_IO_UNIFIED_JUMPTABLES', 'EL2HLT', 'SEM_VALUE_MAX',
           'ME_LOG', 'hypot', 'AVFMT_RAWPICTURE', '_ENDIAN_H',
           'SWS_AREA', 'FF_DTG_AFD_14_9', 'AVSTREAM_PARSE_FULL_ONCE',
           'CODEC_ID_PCM_U32LE', 'AVColorTransferCharacteristic',
           'sws_getCachedContext', 'ftello', 'AVIO_FLAG_DIRECT',
           'initstate', 'timezone', 'AVPROBE_PADDING_SIZE',
           'WEXITSTATUS', 'BYTE_ORDER', 'avdevice_license',
           'isupper_l', 'imaxdiv_t', 'CODEC_ID_R210', 'memmem',
           'ME_X1', 'FF_COMPRESSION_DEFAULT',
           '__SIZEOF_PTHREAD_RWLOCKATTR_T', '__u_quad_t',
           'FF_LOSS_CHROMA', 'PIX_FMT_XVMC_MPEG2_MC',
           'AVMEDIA_TYPE_NB', '_LARGEFILE64_SOURCE', '__uint32_t',
           '_IScntrl', 'av_hwaccel_next', 'avformat_get_class',
           'useconds_t', '__bos0', 'av_flt2int', 'CODEC_ID_WS_VQA',
           'ENOTBLK', 'MB_TYPE_INTRA16x16', 'AVChromaLocation',
           'CODEC_ID_AVUI', '_ISpunct',
           'av_get_default_channel_layout', '__toascii', 'avio_wb24',
           'AV_AUDIO_SERVICE_TYPE_COMMENTARY', 'CODEC_ID_TEXT',
           'MATH_ERREXCEPT', 'offsetof', 'BC_BASE_MAX',
           'CODEC_ID_MP2', 'CODEC_ID_MP3', 'LIBAVCODEC_IDENT',
           'NFDBITS', 'LIBAVCODEC_VERSION_MAJOR', '_POSIX_HIWAT',
           'FF_THREAD_SLICE', 'ENOPKG', 'EOF', 'iscntrl_l',
           'CODEC_ID_AAC', 'AV_CPU_FLAG_SSE', '_G_ssize_t', 'expm1f',
           'obstack_vprintf', 'fsetpos', 'USHRT_MAX', 'expm1l',
           'AV_CH_WIDE_LEFT', 'MAX_REORDER_DELAY', 'AVOutputFormat',
           '_POSIX_UIO_MAXIOV', 'AV_SAMPLE_FMT_S32P', '__signbitf',
           'AVLINK_STARTINIT', 'CODEC_ID_SONIC', 'AV_CH_WIDE_RIGHT',
           'FF_PROFILE_VC1_COMPLEX', 'AV_CH_FRONT_LEFT_OF_CENTER',
           'CODEC_ID_SVQ1', '_G_int16_t', 'CODEC_ID_SVQ3', 'isspace',
           'CODEC_ID_EIA_608', 'CODEC_ID_TSCC',
           'av_packet_shrink_side_data', 'CODEC_FLAG_LOW_DELAY',
           'av_log_ask_for_sample', '_IO_fpos64_t',
           '__mbstate_t_defined', 'FF_PROFILE_MPEG4_SIMPLE',
           'avcodec_get_class', '__time_t_defined', 'avcodec_open',
           '__GLIBC_PREREQ', 'AV_PERM_READ', 'FF_PROFILE_H264_INTRA',
           'avdevice_configuration', 'pid_t', 'ceilf',
           'av_register_codec_parser',
           '_POSIX_THREAD_DESTRUCTOR_ITERATIONS', 'CODEC_ID_MIMIC',
           'avfilter_all_channel_layouts', 'fsfilcnt_t', 'div',
           'round', 'putchar_unlocked', 'cosf', 'nexttoward',
           'avutil_configuration', 'ENOTUNIQ', 'AVCodec', 'cosl',
           'cosh', 'ELNRNG', '__stpcpy', 'CODEC_ID_ALAC', 'sincos',
           'ERESTART', 'ENFILE', 'CODEC_ID_PCM_ALAW',
           'AVFMT_GLOBALHEADER', 'getchar_unlocked', 'AV_LOG_FATAL',
           'AVCOL_SPC_NB', 'ffsll',
           'FF_PROFILE_MPEG4_ADVANCED_CODING', 'erf', 'M_E',
           '__mbstowcs_chk', 'ENOPROTOOPT',
           'FF_PROFILE_H264_CONSTRAINED', '_G_ARGS', 'ME_TESA',
           '_IO_FILE', 'FF_BUFFER_HINTS_REUSABLE', '_G_HAVE_MMAP',
           'va_list', '__attribute_format_strfmon__', 'CODEC_ID_FLAC',
           'CODEC_ID_PCM_U24LE', 'significandl', 'fmax', 'UINT16_C',
           'PIX_FMT_VDPAU_VC1', 'significandf', 'FF_CODER_TYPE_RLE',
           'open_memstream', 'fmaf', 'fsetpos64',
           'av_frame_set_sample_rate', 'fmal', 'exp2l',
           'AVDictionary', 'AV_PICTURE_TYPE_SI', 'lroundf', 'strtok',
           'FF_DCT_MMX', 'lroundl', 'CLOCK_THREAD_CPUTIME_ID',
           'M_LN10', '_G_FSTAT64', 'AV_PICTURE_TYPE_SP',
           'CODEC_FLAG_EMU_EDGE', '_G_HAVE_SYS_WAIT', 'FF_CMP_DCTMAX',
           'CODEC_ID_AURA', 'FF_PROFILE_H264_CONSTRAINED_BASELINE',
           'FF_BUG_STD_QPEL', 'bzero', 'AVFMT_FLAG_NOPARSE',
           'FF_PROFILE_DTS_HD_HRA', 'AV_AUDIO_SERVICE_TYPE_EFFECTS',
           'u_int64_t', 'timer_gettime', '__off_t', 'strptime_l',
           'LIBAVDEVICE_VERSION_INT', 'CODEC_ID_FIRST_UNKNOWN',
           'clock_settime', 'avpicture_alloc',
           'av_probe_input_format2', 'RE_DUP_MAX',
           'CODEC_ID_WMV3IMAGE', 'avcodec_copy_context', 'rindex',
           'PIX_FMT_YUVJ444P', '_IOS_TRUNC', 'CODEC_ID_WMAPRO',
           'AV_PKT_FLAG_KEY', 'av_shrink_packet',
           'AV_DICT_MATCH_CASE', 'FF_BUG_EDGE', 'avcodec_register',
           '__ptsname_r_chk', 'CODEC_ID_PCM_F32BE', '__int8_t',
           'AV_SAMPLE_FMT_FLT', 'AVInputFormat', '_MATH_H',
           'avio_open', 'CODEC_ID_HDMV_PGS_SUBTITLE',
           'av_write_frame', 'ftrylockfile', '_IO_peekc',
           'FF_PROFILE_RESERVED', 'strtoq', '_IO_pid_t',
           'PIX_FMT_YUVJ420P', 'pthread_key_t', 'HUGE_VAL',
           'CODEC_ID_AYUV', 'u_int8_t', 'sws_freeVec',
           'AV_CPU_FLAG_XOP', '_IO_UNITBUF', 'FF_DEBUG_DCT_COEFF',
           'ENOTDIR', 'strtold', 'av_compare_ts',
           'sws_getGaussianVec', 'CODEC_ID_FFWAVESYNTH', 'FF_CMP_W53',
           '__fpclassifyf', 'strtoll', 'MB_TYPE_P0L0', 'feof',
           'strncat', 'CODEC_ID_VOXWARE', 'clearerr', 'ssize_t',
           'av_dup_packet', 'PIX_FMT_RGB444LE', '__CONCAT',
           'ENETRESET', 'CODEC_ID_ADPCM_IMA_WS', '__isprint_l',
           'avfilter_default_query_formats', '_IEEE_',
           'CODEC_ID_DVB_SUBTITLE', 'bsearch', 'flockfile',
           'AVERROR_DEMUXER_NOT_FOUND', 'memrchr',
           'CODEC_ID_NELLYMOSER', 'llround',
           'AVCOL_RANGE_UNSPECIFIED', 'uint',
           'CODEC_FLAG_GLOBAL_HEADER', 'FF_CMP_RD',
           'AVDISCARD_NONREF', '_G_off64_t', 'strncasecmp_l',
           'AVCHROMA_LOC_TOP', 'strcasecmp', 'FF_BUG_UMP4', 'stdin',
           'CODEC_ID_CDGRAPHICS', 'N4wait4DOT_11E',
           'FF_LOSS_RESOLUTION', 'gamma', 'CODEC_ID_AMR_WB',
           'FF_DEBUG_PTS', 'EHOSTUNREACH', '__mempcpy',
           'AVMatrixEncoding', '_G_HAVE_IO_GETLINE_INFO',
           'FF_PROFILE_MPEG4_SCALABLE_TEXTURE',
           'AVFilterBufferRefAudioProps', '_SIGSET_H_types',
           'PIX_FMT_GBRP16LE', 'sws_getColorspaceDetails', 'FILE',
           'size_t', 'seed48', 'MAX_INPUT', 'CODEC_FLAG_4MV',
           'AVMEDIA_TYPE_ATTACHMENT', 'CODEC_ID_RL2',
           'avcodec_get_context_defaults', 'AV_CH_BACK_CENTER',
           'CODEC_ID_PCM_DVD', 'PIX_FMT_BGR8', 'PIX_FMT_VDPAU_MPEG1',
           'PIX_FMT_BGR4', 'M_PI', 'PIX_FMT_VDPAU_MPEG2',
           'CODEC_ID_V308', 'sws_init_context', 'CODEC_ID_FLV1',
           'fileno', '__swblk_t', '__isblank_l', 'PIX_FMT_BGRA',
           'CODEC_ID_PCM_S16LE_PLANAR',
           'avformat_alloc_output_context2', '_MATH_H_MATHDEF',
           'AVFMT_FLAG_IGNIDX', 'av_register_input_format',
           '_LIBC_LIMITS_H_', 'cookie_write_function_t',
           'AVDISCARD_ALL', 'CODEC_ID_ADPCM_EA_XAS',
           'AV_CLASS_CATEGORY_OUTPUT', 'CODEC_ID_APE', 'sigset_t',
           'localtime', '_IO_DELETE_DONT_CLOSE', 'CODEC_ID_RV30',
           'avformat_new_stream', '__isspace_l', '__USE_POSIX',
           'DELAYTIMER_MAX', '__locale_t', 'AV_VERSION',
           'CODEC_ID_FFV1', '_ISalnum', 'SUBTITLE_NONE',
           'CODEC_ID_TTA', 'SCHAR_MIN', 'CODEC_ID_TTF',
           'PIX_FMT_GBRP9LE', '__fd_mask',
           'FF_INPUT_BUFFER_PADDING_SIZE', 'av_parser_parse2',
           'avcodec_encode_video', 'UCHAR_MAX', 'SWS_CPU_CAPS_MMX2',
           'LINE_MAX', 'initstate_r', 'CodecID', '__useconds_t',
           'CODEC_ID_EAC3', '_BITS_WCHAR_H', 'avfilter_unref_bufferp',
           'AV_LOCK_DESTROY', 'CODEC_ID_PCM_S24BE', 'AVLockOp',
           '_POSIX_CLOCKRES_MIN', 'LIBAVUTIL_VERSION_MINOR',
           'AVCHROMA_LOC_BOTTOM', 'FF_DTG_AFD_SP_4_3',
           'uint_least8_t', '__fgets_chk', 'u_int32_t', 'EREMOTE',
           'asprintf', 'FF_CMP_NSSE', '_IO_cookie_io_functions_t',
           'CODEC_CAP_CHANNEL_CONF', '_SYS_TYPES_H', '__P',
           'asctime_r', 'CODEC_ID_SNOW', '_IO_ERR_SEEN', 'remainder',
           'toupper_l', 'FF_PROFILE_DTS', '__uflow',
           'PIX_FMT_GBRP16BE', '__USE_GNU', 'WUNTRACED',
           'avformat_alloc_output_context', 'PIX_FMT_RGB555BE',
           'pthread_attr_t', '__attribute_format_arg__', 'islower',
           'XATTR_LIST_MAX', 'isupper', 'avio_rb16',
           'av_frame_get_best_effort_timestamp',
           'PTHREAD_DESTRUCTOR_ITERATIONS', 'PIX_FMT_YUV420P10BE',
           'CODEC_ID_ADPCM_ADX', 'AV_CH_LAYOUT_2POINT1',
           'CODEC_ID_A64_MULTI', 'avcodec_alloc_context',
           '__W_STOPCODE', 'PIX_FMT_NONE', '__ldiv_t_defined',
           'LIBPOSTPROC_VERSION_MAJOR', 'FF_IDCT_FAAN',
           '_POSIX_MQ_PRIO_MAX', 'strtoll_l', '__W_CONTINUED',
           'sws_isSupportedInput', '__isalpha_l', 'FF_CMP_DCT264',
           'strfry', 'le16toh', 'AVFMT_FLAG_PRIV_OPT',
           'CODEC_ID_MPEG2VIDEO', 'fma', '__mbstate_t',
           'CODEC_ID_ADPCM_SWF', 'PIX_FMT_0BGR', '__toupper_l',
           'AV_FIELD_TT', '_IO_INTERNAL', 'AVFMT_GENERIC_INDEX',
           'av_int2flt', 'j1', 'FF_IDCT_XVIDMMX', 'av_xiphlacing',
           'atanhf', '_G_uid_t', 'SWS_SRC_V_CHR_DROP_MASK',
           'AV_FIELD_TB', 'avformat_free_context', 'av_max_alloc',
           'avcodec_encode_audio', 'avfilter_configuration',
           'AVLINK_INIT', 'quad_t', 'av_frame_set_pkt_duration',
           'MB_TYPE_L1', 'MB_TYPE_L0', '__fsfilcnt64_t',
           'FF_PROFILE_AAC_SSR', 'FF_PROFILE_MPEG2_SNR_SCALABLE',
           'PIX_FMT_YUVA420P', 'INT64_C', 'pthread_cond_t',
           'AVMEDIA_TYPE_AUDIO', 'EPERM', 'RcOverride',
           'TIMER_ABSTIME', 'clock_getres',
           'avcodec_get_frame_defaults', 'av_find_input_format',
           'AVCOL_SPC_RGB', 'gmtime_r', 'nlink_t', 'CODEC_ID_SHORTEN',
           'AVSTREAM_PARSE_TIMESTAMPS', 'AV_JOIN', 'CODEC_ID_V210X',
           'EUNATCH', 'avcodec_default_free_buffers',
           'CLOCKS_PER_SEC', 'WNOWAIT', 'N4wait4DOT_12E',
           'AV_SAMPLE_FMT_U8', 'AV_TOSTRING', 'FF_QSCALE_TYPE_VP56',
           'avcodec_default_get_buffer', 'avcodec_encode_subtitle',
           'AVSTREAM_PARSE_HEADERS', 'realpath', '_POSIX_NAME_MAX',
           'ulong', 'CODEC_ID_CLJR', 'EHWPOISON', 'XATTR_NAME_MAX',
           'av_d2q', 'strpbrk', 'logbf', 'AV_CPU_FLAG_ARMV6T2',
           'logbl', 'CODEC_ID_DXTORY', '__finitel', 'AV_LOG_INFO',
           'CODEC_ID_C93', 'fsblkcnt_t', 'PATH_MAX',
           'av_add_index_entry', 'PixelFormat', 'AV_CH_BACK_RIGHT',
           'AV_GLUE', 'FF_DEBUG_VIS_MB_TYPE',
           'FF_COMPLIANCE_UNOFFICIAL', '__FD_ZERO_STOS', 'vfprintf',
           'WTERMSIG', 'avformat_get_riff_audio_tags', 'isprint_l',
           '_G_HAVE_SYS_CDEFS', 'EDEADLOCK', 'FF_CMP_VSAD',
           'av_guess_codec', 'AV_AUDIO_SERVICE_TYPE_EMERGENCY',
           'timegm', 'AV_DISPOSITION_VISUAL_IMPAIRED', 'nrand48_r',
           'CODEC_CAP_SMALL_LAST_FRAME', 'strtoull',
           'avcodec_default_release_buffer', '_POSIX_LINK_MAX',
           '__finitef', 'ECONNRESET', 'AVCHROMA_LOC_CENTER',
           'av_new_program', 'mkstemps', '__STDC_IEC_559_COMPLEX__',
           'frexp', '_IO_LINE_BUF', 'AV_DISPOSITION_KARAOKE',
           'intptr_t', 'l64a', '_G_config_h', '_IO_FLAGS2_MMAP',
           'M_LN2', 'AVCOL_PRI_BT709', '__GLIBC_HAVE_LONG_LONG',
           'AVStream', '__WCLONE', 'CHAR_MIN', 'CODEC_CAP_LOSSLESS',
           'FF_PROFILE_MPEG4_SIMPLE_SCALABLE',
           'FF_PROFILE_MPEG4_CORE', 'EXPR_NEST_MAX', '_IONBF',
           'be32toh', '_STDLIB_H', 'finitef', '__getdelim',
           'comparison_fn_t', 'av_get_bits_per_sample', 'j0',
           'av_bitstream_filter_filter', 'AVFilterContext', 'qgcvt',
           '__io_read_fn', 'y0', 'av_bprint_channel_layout',
           'sws_cloneVec', 'av_bitstream_filter_next',
           'CODEC_ID_ADPCM_EA', '_POSIX_MQ_OPEN_MAX', 'tanl',
           '_sys_errlist', 'av_index_search_timestamp',
           'CODEC_ID_RV20', 'AV_CH_LAYOUT_5POINT0',
           'AV_CH_LAYOUT_5POINT1', 'avcodec_find_decoder_by_name',
           'lgammal_r', 'ldiv_t', 'vdprintf', 'CODEC_ID_FRWU',
           'setenv', '_POSIX_PIPE_BUF', 'AVFilterBufferRef',
           'CODEC_ID_MLP', 'ECHILD', 'AVFilterGraph',
           'AV_PKT_DATA_H263_MB_INFO', '__USE_XOPEN2K',
           'cookie_read_function_t', 'avcodec_open2', 'jn',
           'FF_BUG_DIRECT_BLOCKSIZE', 'stime', 'AVProfile', 'ME_HEX',
           'av_dict_free', '__qaddr_t', '_IO_LINKED',
           'AV_EF_AGGRESSIVE', 'cbrtl', '__USE_POSIX2', '__blkcnt_t',
           'AV_EF_CRCCHECK', 'CODEC_ID_BINTEXT',
           'av_destruct_packet_nofree', 'CODEC_ID_YOP', 'MB_LEN_MAX',
           'timespec', '__vsnprintf_chk',
           'AV_SIDE_DATA_PARAM_CHANGE_DIMENSIONS', 'vasprintf',
           '_IO_ftrylockfile', 'strxfrm', 'AVCHROMA_LOC_TOPLEFT',
           'ff_log2_tab', 'toupper', 'CODEC_ID_DSICINAUDIO',
           'EBADMSG', 'blkcnt_t', '_ISgraph', 'AV_EF_BITSTREAM',
           'SWS_CS_ITU709', 'clearerr_unlocked', 'av_read_frame',
           'av_register_bitstream_filter', 'CODEC_ID_8BPS',
           'tmpnam_r', 'strtoimax', '_ISalpha', 'ETIMEDOUT',
           'AVCodecDefault', 'av_gcd', 'fread', 'mkostemps64',
           'FF_COMPLIANCE_NORMAL', 'avfilter_merge_formats', 'ENOMSG',
           'AVColorSpace', 'FF_DCT_ALTIVEC', 'SLICE_FLAG_CODED_ORDER',
           'CODEC_ID_ADPCM_IMA_SMJPEG', '_POSIX_DELAYTIMER_MAX',
           'AV_CPU_FLAG_3DNOWEXT', 'FF_QUALITY_SCALE',
           'LIBAVCODEC_VERSION_MICRO', 'scalblnf', 'av_log_get_level',
           'CODEC_ID_VIMA', 'AVFMT_SHOW_IDS', 'vsscanf', 'qfcvt',
           'CODEC_ID_THEORA', 'CODEC_ID_ADPCM_IMA_DK4',
           'avfilter_copy_buffer_ref_props', 'CODEC_ID_XWD', 'stdout',
           'AV_CLASS_CATEGORY_ENCODER', '_STRING_H', '_IO_putc',
           'FF_BUG_MS', 'pp_free_mode',
           'avfilter_make_all_packing_formats', 'AVCOL_SPC_YCOCG',
           '_IO_CURRENTLY_PUTTING', 'av_parse_cpu_flags',
           'AV_CH_TOP_BACK_LEFT', 'yn', 'av_malloc', 'qfcvt_r',
           'fsblkcnt64_t', '_PARAMS', 'EFAULT', 'av_write_trailer',
           'EBADR', 'av_log_set_flags', 'avio_rb24',
           '_OLD_STDIO_MAGIC', '_G_pid_t', 'FF_PROFILE_AAC_LTP',
           'CODEC_ID_MP3ADU', 'toascii_l', 'avfilter_link_free',
           'llroundf', 'avfilter_set_common_packing_formats',
           'AV_DISPOSITION_DUB', 'isnanf', 'av_read_pause', 'calloc',
           'posix_openpt', 'avdevice_register_all', 'isnanl',
           'av_picture_crop', 'avio_rl24', 'EALREADY',
           'AVFilterBufferRefVideoProps', 'AV_CH_LAYOUT_4POINT1',
           'AV_CH_LAYOUT_4POINT0', 'AVERROR_STREAM_NOT_FOUND',
           'fpos64_t', 'fopen64', 'avio_size',
           'FF_PROFILE_MPEG4_HYBRID', 'av_interleaved_write_frame',
           'AV_CH_LAYOUT_5POINT0_BACK', 'PIX_FMT_YUV420P16BE',
           'avio_alloc_context', 'strdup', '__LITTLE_ENDIAN', 'NAN',
           'avfilter_ref_buffer', 'INT16_C', 'CODEC_ID_PRORES',
           'CODEC_ID_V410', 'AVERROR_DECODER_NOT_FOUND',
           'FF_DEBUG_STARTCODE', 'av_sub_q', 'lrintl',
           'AVFMT_TS_NONSTRICT', 'AVCOL_TRC_NB', '_STRUCT_TIMEVAL',
           'timer_delete', 'ptsname', 'avio_put_str16le',
           'CODEC_ID_WMALOSSLESS', 'P_tmpdir',
           'av_frame_set_best_effort_timestamp',
           'CODEC_ID_ADPCM_IMA_QT', '__u_short', 'AV_SAMPLE_FMT_FLTP',
           'scalbf', 'AV_AUDIO_SERVICE_TYPE_MAIN', 'SHRT_MIN',
           'scalbl', '_POSIX_FD_SETSIZE', 'PP_CPU_CAPS_ALTIVEC',
           '_BITS_PTHREADTYPES_H', '_IO_FLAGS2_NOTCANCEL', 'va_start',
           '_G_uint32_t', 'FF_DEBUG_RC', 'CODEC_ID_PCM_U8', 'memmove',
           'SUBTITLE_TEXT', 'av_free', 'av_codec_is_encoder',
           'MB_TYPE_8x8', '__nlink_t', 'avio_wl32', 'TLOSS', 'strcmp',
           'CODEC_ID_G2M', '_POSIX2_BC_BASE_MAX', 'AVDISCARD_DEFAULT',
           'lldiv', 'fgetc', 'gcvt', 'tanhf', 'av_rescale_q',
           'AVCodecParserContext', 'CODEC_ID_PTX',
           'CODEC_ID_ADPCM_SBPRO_2', 'CODEC_ID_ADPCM_SBPRO_3',
           'CODEC_ID_ADPCM_SBPRO_4', 'AVColorRange', 'fgets',
           'ENOSPC', 'NL_LANGMAX', 'cookie_io_functions_t', 'SWS_X',
           'ELIBBAD', 'av_log_missing_feature', 'ERANGE',
           'AVSideDataParamChangeFlags', 'FF_PROFILE_VC1_MAIN',
           'LIBAVFORMAT_VERSION_INT', 'ftell',
           'avfilter_make_all_formats', 'FF_IDCT_IPP',
           'int_least16_t', 'CODEC_CAP_HWACCEL', 'strerror_l',
           'log1pl', 'PIX_FMT_BGR444BE', 'AV_FIELD_PROGRESSIVE',
           'tgammal', 'av_sample_fmt_is_planar', '_SVID_SOURCE',
           'sws_convVec', 'tgammaf', '_CTYPE_H', 'SWS_BICUBIC',
           'CODEC_ID_VMNC', 'avfilter_get_by_name',
           'FF_COMPLIANCE_EXPERIMENTAL', 'AVIOInterruptCB', 'AVERROR',
           'N11__mbstate_t3DOT_7E', 'avdevice_version',
           'AV_CH_FRONT_LEFT', 'CODEC_ID_RV10', 'CODEC_ID_QCELP',
           '__islower_l', 'FF_PRED_PLANE', '__compar_d_fn_t',
           'signgam', 'FF_PROFILE_H264_HIGH_444_INTRA', 'EUSERS',
           'CLOCK_REALTIME', 'nanosleep', 'ENODEV', 'obstack_printf',
           '____FILE_defined', 'avfilter_formats_changeref',
           'AVCOL_SPC_BT470BG', 'avfilter_add_format', 'isgreater',
           '_ERRNO_H', '__SIZEOF_PTHREAD_MUTEX_T',
           'av_get_channel_name', 'SWS_CS_ITU624',
           'av_resample_close', 'OVERFLOW',
           'FF_PROFILE_H264_BASELINE', 'FF_CMP_W97',
           'AVFILTER_PACKED', 'CODEC_ID_VP8', 'putenv',
           'CODEC_ID_VP5', 'CODEC_ID_VP6', 'RAW_PACKET_BUFFER_SIZE',
           'FP_ILOGBNAN', 'CODEC_ID_VP3', 'strtol_l',
           '__sig_atomic_t', 'PIX_FMT_RGB565BE', 'AV_PICTURE_TYPE_P',
           'AV_PICTURE_TYPE_S', 'av_register_hwaccel',
           'avcodec_default_execute2', '__io_seek_fn',
           'avfilter_null_draw_slice', 'UINT64_C', 'avformat_version',
           'sigevent', 'AVChapter', 'AV_PICTURE_TYPE_B',
           'av_get_alt_sample_fmt', 'FF_BUG_AUTODETECT',
           'AV_PICTURE_TYPE_I', 'AVSubtitleRect',
           'LIBAVUTIL_VERSION_MICRO', 'ESHUTDOWN',
           'PIX_FMT_VAAPI_VLD', 'logf', 'FF_IDCT_WMV2',
           'LIBAVFORMAT_IDENT', 'CODEC_ID_COOK', 'tolower_l',
           'AVERROR_OPTION_NOT_FOUND', 'fcvt_r', '_IO_vfscanf',
           '__socklen_t', 'PIX_FMT_YUV444P', 'AVIOContext',
           'FF_PROFILE_MPEG4_ADVANCED_SCALABLE_TEXTURE', 'FD_SET',
           '__isnanl', '__STRING', 'ENOEXEC', '__WCHAR_MIN',
           '__GNUC_PREREQ', 'EBADF', 'EBADE', 'EPROTOTYPE',
           'CODEC_FLAG_CBP_RD', 'sws_alloc_context',
           'avfilter_request_frame', 'AVPALETTE_SIZE',
           '__PTHREAD_MUTEX_HAVE_PREV', 'FF_EC_GUESS_MVS',
           '__PDP_ENDIAN', 'CODEC_FLAG_QP_RD', 'avfilter_uninit',
           'sinhl', 'vfscanf', 'av_add_q', 'PIX_FMT_RGBA64LE',
           'EXDEV', 'avio_w8', '__pid_t', '__va_arg_pack',
           'avio_open2', 'time', '_SIGSET_NWORDS', 'PIX_FMT_GRAY16LE',
           'isinf', 'EBADSLT', 'CODEC_ID_PCM_U16BE',
           'AVMEDIA_TYPE_UNKNOWN', 'CODEC_ID_QPEG',
           'CODEC_FLAG_TRUNCATED', 'sws_shiftVec',
           'FF_DEFAULT_QUANT_BIAS', '__GLIBC_MINOR__',
           '_G_HAVE_ATEXIT', 'difftime', 'CODEC_ID_DNXHD',
           'FF_IDCT_SH4', 'AVPacketSideDataType',
           'AVCHROMA_LOC_UNSPECIFIED', 'CODEC_ID_MP1', 'avio_rb32',
           'av_filename_number_test', 'FF_IDCT_BINK', 'CODEC_ID_SMC',
           'ETOOMANYREFS', '_IO_USER_LOCK', 'int_fast32_t', 'acosl',
           'PIX_FMT_RGBA64BE', 'acosh', 'acosf', 'L_tmpnam',
           'AV_CH_LAYOUT_OCTAGONAL', 'AVERROR_EOF', 'nearbyint',
           'CODEC_ID_ADPCM_IMA_ISS', 'avio_rl32', '__WCOREFLAG',
           'uint8_t', '_G_HAVE_MREMAP', 'CODEC_FLAG_AC_PRED',
           'FF_PROFILE_AAC_LOW', 'strptime', 'EINPROGRESS',
           'L_cuserid', 'mktime', 'tm',
           'CODEC_FLAG2_DROP_FRAME_TIMECODE', '_G_va_list',
           'CODEC_ID_TRUEHD', 'av_dbl2ext', 'makedev',
           '__realpath_chk', 'ENOTSUP', 'AV_LOG_WARNING',
           'CODEC_ID_ADPCM_G722', 'fclose', 'vscanf',
           'CODEC_ID_ADPCM_G726', 'avpicture_deinterlace',
           '__ctype_b_loc', 'CODEC_ID_V408', 'AVFilterChannelLayouts',
           'M_LOG10E', 'CODEC_ID_KGV1', '__WSTOPSIG', 'AVERROR_BUG',
           'EL3RST', 'htole32', 'PARSER_FLAG_USE_CODEC_TS',
           '_POSIX_SOURCE', '_IO_jump_t', '_ISdigit', 'stderr',
           'ENAMETOOLONG', 'fputc_unlocked', 'AVPanScan',
           '__uint64_t', 'FF_PROFILE_DTS_HD_MA', 'M_PI_4',
           'AV_AUDIO_SERVICE_TYPE_VOICE_OVER',
           'AVFMT_DURATION_FROM_PTS', 'FF_DTG_AFD_SAME', 'scalblnl',
           '_IO_off_t', '__clockid_t', 'PIX_FMT_VDPAU_H264', 'nanl',
           'clock', 'y1f', 'FF_BUG_QPEL_CHROMA', 'AVDISCARD_BIDIR',
           'abs', 'AVPicture', 'AV_CH_TOP_FRONT_CENTER',
           '__WEXITSTATUS', 'LIBAVCODEC_BUILD', 'avio_wl24',
           'AVERROR_INVALIDDATA', '_IO_pos_t', 'CODEC_ID_MPEG2TS',
           '_ISxdigit', 'FF_DEBUG_VIS_QP', 'avcodec_is_open',
           'SWS_BITEXACT', 'lgammaf_r', 'avfilter_init_filter',
           'CLOCK_REALTIME_COARSE', 'stpncpy',
           '_POSIX_THREAD_KEYS_MAX', 'CODEC_ID_BMP',
           'av_get_channel_layout_channel_index', 'fsid_t',
           '__WIFEXITED', 'AVBitStreamFilterContext',
           'CODEC_ID_ADPCM_IMA_DK3', 'FF_DTG_AFD_4_3', 'rename',
           'CODEC_ID_BETHSOFTVID', '_IO_ferror', 'isspace_l', 'log2l',
           'PIX_FMT_MONOBLACK', 'ERFKILL', '__mode_t',
           'avfilter_null_start_frame', 'FF_DCT_FAAN',
           'FF_LEVEL_UNKNOWN', 'FF_BUFFER_TYPE_INTERNAL',
           'CODEC_ID_TGV', 'AV_CPU_FLAG_MMX2', 'select',
           'CODEC_ID_TGQ', 'AVFMT_NOFILE', 'canonicalize_file_name',
           '__W_EXITCODE', 'cfree', 'AV_SAMPLE_FMT_U8P',
           'CODEC_ID_NONE', 'FF_BUG_NO_PADDING', '_POSIX_MAX_INPUT',
           'avfilter_draw_slice', 'isless', 'minor', 'exp10',
           'log10f', 'isunordered', '__USE_FORTIFY_LEVEL',
           'CODEC_ID_ADPCM_IMA_EA_SEAD', 'CODEC_ID_QDRAW',
           'fwrite_unlocked', 'CODEC_ID_WAVPACK', 'PIX_FMT_Y400A',
           'pthread_barrierattr_t', 'PIX_FMT_BGR24',
           'av_resample_init', 'fopencookie',
           'avformat_configuration', '__uint16_t', 'AVHWAccel',
           'avfilter_process_command', '__bzero', 'localtime_r',
           'SWS_DIRECT_BGR', 'roundl', 'CODEC_FLAG2_FAST',
           'FF_MIN_BUFFER_SIZE', 'CODEC_ID_FIRST_AUDIO',
           'pp_postprocess', 'M_1_PI', 'SWS_SINC', 'PIPE_BUF',
           'avfilter_set_common_channel_layouts',
           'AV_PKT_DATA_PARAM_CHANGE', 'LIBSWSCALE_VERSION_MAJOR',
           'CODEC_FLAG_PSNR', 'av_set_pts_info', 'AVCodecContext',
           'atanf', 'M_2_PI', 'erff', 'atanh', 'atanl',
           'EAFNOSUPPORT', 'avio_close_dyn_buf', 'putc_unlocked',
           'CODEC_FLAG_CLOSED_GOP', 'time_t', 'AV_CPU_FLAG_3DNOW',
           'AV_AUDIO_SERVICE_TYPE_KARAOKE', 'mrand48_r', 'srand48_r',
           'AVCOL_PRI_BT470BG', 'avfilter_default_get_video_buffer',
           'clock_nanosleep', 'av_get_output_timestamp',
           'FF_IDCT_SIMPLEARM', 'AV_PROGRAM_RUNNING', '__rlim64_t',
           'AV_SAMPLE_FMT_DBL', 'fabs', 'AV_STRINGIFY', 'ino_t',
           'AVFMT_NEEDNUMBER', 'AV_NOPTS_VALUE', 'atan2', '_ISspace',
           '__clock_t', 'AVExtFloat', '__fsfilcnt_t', 'ENOCSI',
           'coshf', 'tan', '__STDLIB_MB_LEN_MAX', 'rand', 'coshl',
           'LIBAVFORMAT_BUILD', 'basename', 'ffs', '__LONG_LONG_PAIR',
           '__WCOREDUMP', 'sqrt', 'ferror_unlocked', 'y1', 'EAGAIN',
           '__error_t_defined', 'XATTR_SIZE_MAX', 'AVRounding',
           'ELIBEXEC', 'sws_scale', 'FF_LAMBDA_MAX',
           'AVFMT_NOTIMESTAMPS', 'roundf', 'LIBAVCODEC_VERSION_INT',
           '_POSIX2_LINE_MAX', 'EIO', 'CODEC_FLAG_INPUT_PRESERVED',
           'feof_unlocked', '_G_HAVE_LONG_DOUBLE_IO', 'remquo',
           '_POSIX_MAX_CANON', 'memchr', 'PIX_FMT_YUV411P',
           'avfilter_insert_inpad', '_IOS_APPEND', 'SWS_GAUSS',
           'FF_PRED_MEDIAN', '_POSIX_THREAD_THREADS_MAX',
           '__asprintf_chk', 'strcoll', 'CODEC_ID_PCM_MULAW',
           '_G_BUFSIZ', 'ynl', 'gets', 'LIBAVUTIL_VERSION_MAJOR',
           'ynf', '__blksize_t', 'CODEC_ID_AVRP', 'AVFilterLink',
           'fmod', 'EDESTADDRREQ', 'LIBAVFILTER_BUILD', 'getw', 'pow',
           'pp_get_context', 'avcodec_align_dimensions',
           'sws_get_class', '_XOPEN_LIM_H', 'CODEC_ID_8SVX_FIB',
           'isalnum_l', 'ENETUNREACH', '_XOPEN_IOV_MAX',
           'AV_LOCK_RELEASE', 'rintl', '_G_NAMES_HAVE_UNDERSCORE',
           '_IO_NO_READS', '_POSIX_AIO_LISTIO_MAX', 'AVFormatContext',
           'CODEC_ID_PROBE', '__snprintf_chk', 'FF_DEBUG_BUGS',
           'CODEC_ID_MSS1', 'strrchr', '__strtok_r',
           'pthread_barrier_t', 'pthread_rwlock_t', 'strchrnul',
           'tzset', '__pthread_internal_list', 'av_filter_next',
           'labs', 'avformat_write_header', 'FP_ILOGB0',
           'FF_IDCT_SIMPLE', 'CODEC_ID_NUV', 'qsort_r',
           '_G_VTABLE_LABEL_HAS_LENGTH', '_BITS_POSIX2_LIM_H',
           'CODEC_ID_PCM_S8', 'AV_CH_LAYOUT_7POINT1_WIDE', 'putchar',
           'LIBAVFILTER_VERSION_MICRO', 'SLICE_FLAG_ALLOW_FIELD',
           'getc_unlocked', 'CODEC_ID_S302M', 'av_hex_dump',
           'avio_wl16', '__vsprintf_chk', 'major',
           'CODEC_CAP_TRUNCATED', 'FF_IDCT_INT',
           'AVERROR_MUXER_NOT_FOUND', 'pthread_spinlock_t',
           '_IO_seekoff', 'setbuf', '__isnanf',
           'FF_PROFILE_MPEG4_ADVANCED_SIMPLE', 'strtoull_l',
           '_IO_sgetn', 'ecvt', 'CODEC_ID_TARGA', 'CODEC_ID_UTVIDEO',
           'avfilter_set_common_formats', 'avfilter_insert_pad',
           '__asprintf', 'free', '__toascii_l',
           'CODEC_ID_WESTWOOD_SND1', 'AVCodecParser', 'av_match_ext',
           'nearbyintf', 'AVIO_FLAG_WRITE', 'avio_check', 'llrint',
           'AVCHROMA_LOC_NB', '_IOS_NOCREATE', '_Exit',
           'AV_ERROR_MAX_STRING_SIZE', 'CODEC_ID_IDCIN', 'FF_DCT_INT',
           'audio_resample_close', 'CODEC_ID_VCR1', 'MB_TYPE_ACPRED',
           'CODEC_ID_XAN_WC3', 'av_get_media_type_string',
           '__isupper_l', 'AVFilterCommand', '__USE_LARGEFILE',
           'SWS_MAX_REDUCE_CUTOFF', '_FEATURES_H', 'strcasestr',
           'CODEC_CAP_EXPERIMENTAL', 'CODEC_ID_SP5X', 'CODEC_ID_R10K',
           'vsnprintf', '_IO_peekc_locked', '_POSIX_SEM_NSEMS_MAX',
           'CODEC_ID_ILBC', 'nearbyintl', 'CODEC_FLAG2_CHUNKS',
           'pselect', 'CODEC_ID_TXD', 'avformat_seek_file',
           'av_frame_get_sample_rate', 'SING', '__fread_chk',
           'EPFNOSUPPORT', 'sys_nerr', 'AV_PERM_ALIGN', 'strtoul_l',
           '_POSIX_PATH_MAX', 'CODEC_ID_DPX', 'PP_FORMAT_411',
           'timeval', 'CODEC_ID_RA_288', '__int64_t',
           'FF_PROFILE_MPEG2_422', 'av_get_channel_layout',
           'AVCOL_TRC_BT709', '_IO_UNBUFFERED',
           'CODEC_ID_BINKAUDIO_RDFT', 'CODEC_ID_YUV4',
           'avformat_network_deinit', 'av_iformat_next',
           'significand', 'index', 'AV_PERM_REUSE2', 'av_parser_next',
           'LOGIN_NAME_MAX', '__WIFSTOPPED', 'avio_get_str', 'nan',
           'EL2NSYNC', 'exp', '__MATHCALLX',
           'LIBAVDEVICE_VERSION_MINOR', 'strncasecmp', 'SWS_BICUBLIN',
           'PIX_FMT_YUV410P', 'isascii', 'CODEC_ID_GSM_MS',
           'AVProgram', 'av_parser_init', 'pp_help',
           'AVSTREAM_PARSE_FULL', 'mode_t', 'FF_MB_DECISION_SIMPLE',
           'rintf', 'FF_PROFILE_MPEG2_SS', 'isascii_l',
           'CODEC_ID_Y41P', '_POSIX_SSIZE_MAX', 'grantpt', '__isinff',
           'ESTRPIPE', 'fputs', 'lrand48_r', 'FF_DEBUG_BUFFERS',
           'strtof_l', 'avcodec_find_encoder_by_name',
           'SUBTITLE_BITMAP', '_IO_TIED_PUT_GET', 'AV_NE',
           'AVCodecInternal', 'CODEC_FLAG_NORMALIZE_AQP', 'EDEADLK',
           'FD_CLR', 'id_t', 'PIX_FMT_GRAY8A', 'tgamma',
           'CODEC_ID_INTERPLAY_VIDEO', 'cookie_seek_function_t',
           'PIX_FMT_BGR565LE', 'av_realloc_f',
           'FF_BUFFER_TYPE_SHARED', 'strtod_l', 'AV_PERM_PRESERVE',
           'FP_NAN', 'av_ext2dbl', 'FOPEN_MAX', 'PIX_FMT_BGR555LE',
           'remove', 'CODEC_ID_ULTI', 'avutil_license', 'fd_mask',
           'AV_ROUND_DOWN', '__int16_t', 'CODEC_ID_TWINVQ',
           'FF_PROFILE_MPEG4_CORE_SCALABLE', 'mbtowc', 'sinf',
           'AV_CH_SIDE_RIGHT', 'isalpha_l', 'FF_IDCT_H264',
           'quick_exit', '__FDELT', 'AV_MATRIX_ENCODING_NB',
           'avio_rl16', 'CODEC_ID_TRUESPEECH', 'strchr',
           '_POSIX_TZNAME_MAX', 'MB_TYPE_CBP',
           'av_get_sample_fmt_string', 'AVClass',
           'avfilter_set_common_sample_formats',
           'AV_CH_TOP_FRONT_RIGHT', 'FF_BUFFER_TYPE_USER',
           'WIFCONTINUED', 'PP_PICT_TYPE_QP2', 'y0f', 'atoll',
           'FF_PROFILE_MPEG4_N_BIT', 'FF_DEBUG_ER',
           'av_channel_layout_extract_channel',
           'AV_DICT_IGNORE_SUFFIX', 'AV_PKT_FLAG_CORRUPT',
           'sws_allocVec', 'sws_normalizeVec', 'CODEC_ID_SANM',
           'htole16', 'FF_PROFILE_VC1_ADVANCED',
           'av_samples_fill_arrays', 'FF_DEBUG_PICT_INFO',
           'PIX_FMT_GRAY8', '__timespec_defined',
           'N16pthread_rwlock_t4DOT_25E', 'CODEC_ID_PCM_BLURAY',
           'avfilter_pad_get_type', 'y0l', 'av_find_best_stream',
           'FF_PROFILE_H264_HIGH_444_PREDICTIVE', 'timer_settime',
           'timer_getoverrun', 'CODEC_ID_MPEG4SYSTEMS',
           '_IO_flockfile', 'av_packet_get_side_data', 'acoshf',
           'fflush_unlocked', 'double_t', 'CODEC_ID_PGM',
           'AVFilterPad', 'alloca', 'CODEC_ID_ATRAC3', 'EREMCHG',
           'FF_DTG_AFD_16_9_SP_14_9', '__BIT_TYPES_DEFINED__',
           'MAX_PROBE_PACKETS', 'sqrtf', '_IO_RIGHT', '__u_long',
           'ENOMEM', 'FF_IDCT_SIMPLEARMV5TE', '__wcstol_internal',
           '_BITS_TYPES_H', 'EOWNERDEAD', 'wait', 'M_2_SQRTPI',
           '__exception', 'AV_DICT_DONT_STRDUP_KEY',
           'CODEC_ID_JPEG2000', 'asinl', 'asinf', 'EILSEQ',
           'AVFMT_SEEK_TO_PTS', '__ino64_t', 'strtok_r',
           'AVIO_FLAG_NONBLOCK', 'CODEC_ID_AAC_LATM', 'ULLONG_MAX',
           'AVCODEC_MAX_AUDIO_FRAME_SIZE', 'asinh',
           'avcodec_default_get_format', 'itimerspec',
           'CODEC_CAP_NEG_LINESIZES', 'malloc',
           'AV_CLASS_CATEGORY_FILTER', 'M_PI_2',
           'AVFMT_FLAG_SORT_DTS', '_IO_uid_t', 'FF_IDCT_MMI',
           'AV_CH_SURROUND_DIRECT_RIGHT', 'INT32_C',
           'AV_SIDE_DATA_PARAM_CHANGE_CHANNEL_COUNT',
           'CODEC_FLAG_PASS2', 'CODEC_ID_VMDVIDEO', 'drand48_data',
           'postproc_configuration', 'error_t', 'avio_read',
           'EWOULDBLOCK', '__USE_XOPEN2K8XSI', 'PLOSS', '_G_size_t',
           'CODEC_ID_CYUV', 'nextafter', 'va_copy', 'scalbn',
           'PP_FORMAT', '_IO_IS_FILEBUF', 'SEEK_SET', '__io_write_fn',
           '_IOS_OUTPUT', 'SUBTITLE_ASS', 'sws_getContext',
           'sws_printVec2', 'srandom_r', 'CODEC_ID_ADPCM_EA_R1',
           'CODEC_ID_ADPCM_EA_R2', 'av_get_channel_layout_string',
           'CODEC_ID_MACE3', 'program_invocation_short_name',
           '_G_HAVE_BOOL', 'CODEC_ID_MACE6', 'NAME_MAX',
           'av_packet_split_side_data', 'CODEC_FLAG2_SHOW_ALL',
           'uint32_t', 'FF_QSCALE_TYPE_MPEG1', '_LARGEFILE_SOURCE',
           'ff_get_cpu_flags_x86', 'mempcpy', 'M_SQRT1_2',
           'CODEC_ID_8SVX_RAW', 'AV_PERM_NEG_LINESIZES',
           'av_log_default_callback', '__isdigit_l',
           'av_hex_dump_log', '_G_off_t', 'av_find_nearest_q_idx',
           'CODEC_ID_AURA2', 'dreml', 'fflush',
           'av_get_planar_sample_fmt', 'AVIO_FLAG_READ_WRITE',
           'CODEC_ID_MJPEGB', 'CODEC_ID_MSRLE', 'AV_CPU_FLAG_ATOM',
           'CODEC_ID_PCM_S8_PLANAR', 'CODEC_ID_DVB_TELETEXT',
           'realloc', 'CODEC_ID_ANSI', 'CODEC_ID_CSCD', 'ENOLCK',
           'SWS_POINT', 'LIBPOSTPROC_IDENT', 'exp10l',
           'AV_SIDE_DATA_PARAM_CHANGE_CHANNEL_LAYOUT',
           '_IO_SHOWPOINT', 'av_pkt_dump_log2', 'CODEC_ID_XSUB',
           'FF_BUG_TRUNCATED', 'exp10f', 'AV_CPU_FLAG_MMX',
           '__fread_unlocked_chk', 'CODEC_FLAG_INTERLACED_DCT',
           'avcodec_get_edge_width', 'N8AVPacket4DOT_31E',
           '_POSIX2_RE_DUP_MAX', 'LIBSWSCALE_VERSION_MINOR',
           'register_t', 'postproc_license', 'CODEC_ID_CMV', 'strstr',
           'renameat', '__fgets_unlocked_chk', '_POSIX_TIMER_MAX',
           'mblen', 'PIX_FMT_YUV444P10BE', 'AVCHROMA_LOC_BOTTOMLEFT',
           '_IO_vfprintf', 'ESRCH', 'remquol', 'PIX_FMT_VDA_VLD',
           'tmpfile', 'AVFMTCTX_NOHEADER', 'fd_set', 'PIX_FMT_GBRP',
           'CODEC_CAP_DR1', 'remquof', 'mrand48', 'FF_CMP_VSSE',
           'FF_PROFILE_MPEG4_ADVANCED_REAL_TIME', 'intmax_t',
           'av_destruct_packet', 'CODEC_ID_DVVIDEO', '_IO_SHOWPOS',
           'fmemopen', 'CODEC_ID_MXPEG', 'av_force_cpu_flags',
           'CODEC_ID_ROQ_DPCM', 'av_fast_realloc', 'AVFMT_TS_DISCONT',
           'AVCOL_TRC_SMPTE240M', 'scalb', 'int_least8_t',
           '_LIB_VERSION_TYPE', 'AV_VERSION_INT',
           'AV_DICT_DONT_STRDUP_VAL', '__signbitl', 'FFMAX3',
           'av_probe_input_format3', 'AVERROR_ENCODER_NOT_FOUND',
           '__vfprintf_chk', 'isgreaterequal', '_G_uint16_t',
           'ENOBUFS', 'AVFMT_FLAG_IGNDTS', '_BITS_POSIX1_LIM_H',
           'FP_SUBNORMAL', 'AV_CH_LAYOUT_6POINT0_FRONT',
           'CODEC_ID_FFVHUFF', 'PIX_FMT_YUV444P16LE',
           'avio_seek_time', 'FF_BUG_XVID_ILACE',
           'FF_PROFILE_VC1_SIMPLE', 'SWS_CPU_CAPS_ALTIVEC', 'putw',
           'CODEC_ID_ZMBV', 'FF_IDCT_ARM', '__USE_BSD',
           'FF_EC_DEBLOCK', 'dremf', 'AV_MATRIX_ENCODING_DOLBY',
           'av_sdp_create', 'FFMIN3', 'fmin', 'ptrdiff_t',
           '_IOS_NOREPLACE', 'tanhl', 'avio_pause', '__ispunct_l',
           'AV_CPU_FLAG_AVX', 'SEEK_CUR', '_POSIX_CHILD_MAX',
           'EOPNOTSUPP', 'sqrtl', 'fopen', 'FF_PROFILE_H264_HIGH_444',
           'CODEC_ID_GSM', 'CODEC_ID_RPZA', 'memccpy',
           'AV_CH_LAYOUT_SURROUND', 'errno', 'lround',
           'avformat_license', 'PIX_FMT_BGR48BE', 'ReSampleContext',
           'daddr_t', '_IO_cookie_file', 'AV_DISPOSITION_COMMENT',
           'ME_ZERO', 'sws_getDefaultFilter', 'AVIO_FLAG_READ',
           'vprintf', 'av_oformat_next', 'CODEC_ID_MUSEPACK8',
           'CODEC_ID_MUSEPACK7', 'AVFMT_FLAG_KEEP_SIDE_DATA',
           'int8_t', 'avsubtitle_free', 'CODEC_ID_IMC', 'atoi',
           '_IO_funlockfile', 'CODEC_ID_LAGARITH',
           'AV_AUDIO_SERVICE_TYPE_VISUALLY_IMPAIRED', 'atof',
           'AV_LOCK_OBTAIN', 'ESPIPE', 'AVSEEK_FLAG_FRAME', 'erand48',
           'CODEC_ID_MPEG2VIDEO_XVMC', 'PP_QUALITY_MAX', 'fdim',
           'daylight', 'AVSTREAM_PARSE_FULL_RAW', 'CODEC_ID_SOL_DPCM',
           'EMSGSIZE', 'imaxdiv', 'avformat_query_codec',
           'avcodec_get_context_defaults3', 'ungetc',
           'FF_ARRAY_ELEMS', 'EROFS', 'blkcnt64_t', 'ffsl', 'lrint',
           'AVCOL_SPC_UNSPECIFIED', '_STDIO_H',
           'cookie_close_function_t', 'postproc_version', 'isdigit',
           'COLL_WEIGHTS_MAX', 'sws_subVec', '_POSIX_QLIMIT',
           'avformat_get_riff_video_tags', 'AV_VERSION_DOT',
           'ELIBACC', 'CODEC_ID_PPM', 'av_fast_malloc',
           'LIBAVUTIL_IDENT', 'AV_LOG_SKIP_REPEATED',
           'PIX_FMT_BGR444LE', 'av_set_cpu_flags_mask',
           '_POSIX_RE_DUP_MAX', 'CODEC_ID_VC1IMAGE',
           'AVSEEK_FLAG_BYTE', 'fmodf', 'fmodl', 'ENAVAIL',
           'AVDiscard', 'CODEC_FLAG_INTERLACED_ME',
           'av_get_cpu_flags', '_G_NEED_STDARG_H',
           '__ctype_toupper_loc', 'PIX_FMT_RGB4_BYTE',
           '__va_arg_pack_len', 'BC_SCALE_MAX', 'mkostemp64', 'exp2f',
           'avformat_find_stream_info', '_G_VTABLE_LABEL_PREFIX',
           'CODEC_FLAG_MV0', 'CODEC_ID_LJPEG',
           'avcodec_fill_audio_frame', 'isnan', 'EIDRM', 'INT_MIN',
           'EOVERFLOW', 'AVFILTER_CMD_FLAG_ONE', '__codecvt_noconv',
           'FF_DEBUG_SKIP', 'AVFMT_DURATION_FROM_BITRATE',
           'avfilter_open', '_ATFILE_SOURCE',
           'av_samples_get_buffer_size', '__pthread_mutex_s',
           'avcodec_find_best_pix_fmt2', 'LONG_MIN',
           'PIX_FMT_GBRP9BE', 'ldexpl', 'CODEC_FLAG_GRAY',
           'av_get_packet', '_POSIX_OPEN_MAX', 'ldexpf', 'FF_IDCT_EA',
           'LIBAVDEVICE_BUILD', 'log2f', 'fpos_t',
           'AV_CPU_FLAG_ARMV6', 'ME_ITER', 'CODEC_ID_ANM',
           'av_reverse', 'atan2l', 'va_end', 'llrintf',
           'avcodec_get_subtitle_rect_class',
           'FF_PROFILE_H264_CAVLC_444', '__SIZEOF_PTHREAD_CONDATTR_T',
           'getline', 'FF_DCT_FASTINT', 'random', 'scalbnf',
           'CODEC_ID_SPEEX', 'AVFilter', 'scalbnl', 'erand48_r',
           'av_read_play', 'MB_TYPE_16x8', 'CODEC_ID_THP',
           'CODEC_ID_VIXL', '__ASMNAME', 'ME_FULL', 'UINT8_C',
           'AV_ROUND_NEAR_INF', 'mbstowcs', 'EREMOTEIO',
           'CODEC_ID_H264', 'CODEC_ID_H261', 'CODEC_ID_H263',
           'CODEC_ID_XBM', 'isblank', 'ferror', 'snprintf',
           '_ALLOCA_H', 'avcodec_close', 'memset', 'CODEC_ID_SSA',
           'AV_CH_LAYOUT_NATIVE', '__ctype_get_mb_cur_max',
           'UINTMAX_C', '__USE_POSIX199309', 'avcodec_flush_buffers',
           'mktemp', 'FF_IDCT_SIMPLEALPHA', 'CODEC_ID_ADPCM_IMA_WAV',
           'av_get_sample_fmt_name', 'AV_CH_FRONT_CENTER', 'ENOANO',
           'EUCLEAN', 'CODEC_ID_LOCO', 'NGROUPS_MAX',
           'CODEC_FLAG2_LOCAL_HEADER', '_G_fpos_t',
           'avfilter_unref_buffer', 'CODEC_ID_ESCAPE130', 'log1pf',
           'fputc', '__lldiv_t_defined', '__SIZEOF_PTHREAD_BARRIER_T',
           'sinl', 'sinh', 'av_codec_is_decoder', '_IOS_BIN',
           '_ISblank', 'acoshl', '_ISupper', 'CODEC_ID_VC1',
           'AVERROR_UNKNOWN', 'ME_EPZS', '__printf_chk',
           'PIX_FMT_BGR555BE', 'CODEC_ID_CAVS', 'AV_EF_EXPLODE',
           '__locale_struct', '__PMT', 'uint_fast8_t',
           'av_bitstream_filter_init', 'BC_STRING_MAX', 'EPIPE',
           'pp_mode', 'EBFONT', '__WALL', 'AVFilterFormats',
           '_IO_DONT_CLOSE', 'avpicture_fill', 'EADDRINUSE',
           'AVIO_SEEKABLE_NORMAL', '__WNOTHREAD', 'fdimf',
           'fsfilcnt64_t', 'fdiml', 'FF_DEBUG_BITSTREAM', '_IOFBF',
           'AVFMT_FLAG_GENPTS', 'AV_CH_BACK_LEFT', 'wcstoimax',
           'int_least64_t', 'avcodec_align_dimensions2',
           'CODEC_ID_PCM_S16BE', 'islower_l', 'nexttowardf',
           'LIBAVDEVICE_VERSION_MAJOR', 'FF_IDCT_ALTIVEC',
           'isgraph_l', 'nexttowardl', 'LIBPOSTPROC_VERSION_MINOR',
           'CODEC_ID_JV', 'llrintl', 'ENOENT', 'CODEC_CAP_SUBFRAMES',
           'BIG_ENDIAN', 'MB_TYPE_8x16', '__USE_XOPEN_EXTENDED',
           'PP_FORMAT_444', 'strftime_l', 'av_get_codec_tag_string',
           'AV_PERM_REUSE', 'ECOMM', 'mkostemps', 'PIX_FMT_GBRP10LE',
           'AV_CH_LOW_FREQUENCY', 'abort', 'PIX_FMT_YUVA444P',
           'FD_ZERO', '__loff_t', 'ENOTEMPTY', 'CODEC_ID_AVS',
           'UNDERFLOW', 'fprintf', 'CODEC_ID_PAM',
           'CODEC_ID_PCM_S16LE', 'AV_CLASS_CATEGORY_NA',
           'AV_CLASS_CATEGORY_NB', 'av_mallocz', '_POSIX_SYMLINK_MAX',
           'HUGE', 'FF_THREAD_FRAME', '__WIFCONTINUED',
           '__wcstombs_chk', 'lcong48', 'EBADRQC', 'av_printf_format',
           'CODEC_ID_ADPCM_4XM', 'avio_wl64', 'AV_CPU_FLAG_SSE4',
           'AV_CPU_FLAG_SSE3', 'CODEC_ID_VMDAUDIO', 'on_exit', 'sin',
           'CODEC_CAP_PARAM_CHANGE', 'WEXITED', 'av_freep',
           '_IO_free_backup_area', 'CODEC_ID_EXR', 'LONG_LONG_MIN',
           'gammaf', '__USE_ISOC95', 'CODEC_ID_XAN_WC4',
           'FF_FDEBUG_TS', 'ceil', 'CODEC_ID_AMR_NB', '__USE_ISOC99',
           'CODEC_ID_VORBIS', 'EMEDIUMTYPE', '_IO_fpos_t',
           '_G_USING_THUNKS', 'av_dict_get', 'ENOKEY', 'rawmemchr',
           'CODEC_CAP_DRAW_HORIZ_BAND', 'avformat_network_init',
           'strsep', 'EPROTONOSUPPORT', 'le32toh', 'avio_write',
           'ETIME', 'AV_CH_SURROUND_DIRECT_LEFT', '_INTTYPES_H',
           'av_lockmgr_register', 'jnf', 'AVOption', 'CODEC_ID_RV40',
           '__USE_XOPEN', 'AV_CH_TOP_BACK_RIGHT', 'AV_EF_CAREFUL',
           'AV_DISPOSITION_DEFAULT', 'FF_PROFILE_MPEG2_SIMPLE',
           'PARSER_FLAG_COMPLETE_FRAMES', 'CODEC_ID_MP4ALS',
           'AVFILTER_ALIGN', 'CODEC_ID_SONIC_LS', 'AV_CPU_FLAG_SSE2',
           'CODEC_ID_FRAPS', 'AV_CH_LAYOUT_STEREO', 'islessequal',
           'LITTLE_ENDIAN', 'AV_LOG_ERROR', '__USE_ATFILE', 'TMP_MAX',
           'PIX_FMT_YUV422P9LE', 'swscale_license', 'PP_FORMAT_420',
           'PP_FORMAT_422', 'AV_CPU_FLAG_CMOV', 'PIX_FMT_YUYV422',
           '__int32_t', 'modf', 'av_alloc_size', 'EADDRNOTAVAIL',
           'FF_DEBUG_MMCO', '_IO_NO_WRITES', 'avfilter_end_frame',
           'LIBPOSTPROC_VERSION_INT', 'random_data',
           'SWS_CPU_CAPS_3DNOW', 'CODEC_ID_SIPR', 'CODEC_ID_MPEG4',
           '__FILE_defined', '_IO_STDIO', 'AVCOL_RANGE_MPEG',
           'clock_t', 'int_fast64_t', 'EISCONN', 'isdigit_l', 'atan',
           'AVCOL_PRI_UNSPECIFIED', 'FF_PROFILE_DTS_96_24',
           'CODEC_ID_PCM_U24BE', 'AV_TIME_BASE', 'av_codec_get_id',
           'CODEC_FLAG_QSCALE', 'FF_BUFFER_TYPE_COPY', 'unsetenv',
           'AV_PICTURE_TYPE_NONE', '__BYTE_ORDER', 'av_codec_get_tag',
           'av_default_item_name', 'atan2f', 'SWS_CPU_CAPS_BFIN',
           'AVPROBE_SCORE_MAX', '__signbit',
           'FF_PROFILE_MPEG4_ADVANCED_CORE', 'CODEC_ID_G729',
           'FF_PROFILE_H264_EXTENDED', 'PIX_FMT_YUV420P9LE',
           '__gnuc_va_list', 'CODEC_ID_FLASHSV2',
           'avfilter_default_end_frame', 'fseeko',
           'CODEC_ID_SMACKVIDEO', 'key_t', 'CODEC_ID_FLIC',
           'random_r', 'isinff', 'fdopen', 'AV_CPU_FLAG_ARMV5TE',
           '_G_IO_IO_FILE_VERSION', 'ELIBMAX', '_POSIX_C_SOURCE',
           '__daylight', 'AV_PKT_DATA_PALETTE', 'EMULTIHOP',
           'CODEC_ID_ESCAPE124', '_IO_ssize_t',
           'AV_HAVE_FAST_UNALIGNED', 'bcopy', '__caddr_t',
           '_POSIX2_CHARCLASS_NAME_MAX', '__USE_SVID',
           'av_get_pcm_codec', 'CODEC_ID_XBIN',
           'AV_CH_LAYOUT_7POINT0_FRONT', '_IO_IS_APPENDING',
           'AV_SAMPLE_FMT_NB', 'copysignf', 'AVLINK_UNINIT',
           'FF_DEBUG_THREADS', 'CODEC_ID_PCM_F32LE', 'copysignl',
           'M_LOG2E', 'system',
           'av_fmt_ctx_get_duration_estimation_method',
           '__bswap_constant_32', 'WSTOPPED', 'ECONNABORTED',
           'L_ctermid', 'EINVAL', 'mkstemp64', '__errno_location',
           'CODEC_ID_8SVX_EXP', '__uint8_t',
           '__SIZEOF_PTHREAD_RWLOCK_T', 'av_rescale_rnd', 'strcat',
           'AVFMT_DURATION_FROM_STREAM', '__obstack_printf_chk',
           'av_strdup', 'avpicture_free', 'CODEC_ID_RALF',
           'HOST_NAME_MAX', 'FF_PROFILE_MPEG2_HIGH', 'fscanf',
           'log10', '__USE_EXTERN_INLINES', '__SIZEOF_PTHREAD_COND_T',
           'toascii', 'av_interleave_packet_per_dts',
           'FF_COMPLIANCE_STRICT', 'FF_BUG_DC_CLIP',
           '__REDIRECT_NTH_LDBL', 'EDOM', 'AV_CPU_FLAG_ALTIVEC',
           'NL_ARGMAX', 'av_samples_copy', 'uintptr_t', 'avio_close',
           'FF_COMPLIANCE_VERY_STRICT', 'FP_ZERO',
           'FF_PROFILE_H264_HIGH_422', 'PIX_FMT_YUV420P',
           'CODEC_ID_MSMPEG4V2', 'CODEC_ID_MSMPEG4V3', 'av_dict_set',
           'CODEC_ID_MSMPEG4V1', 'rint', 'CODEC_ID_H263I',
           '_XOPEN_SOURCE_EXTENDED', 'CODEC_ID_H263P',
           'AV_MATRIX_ENCODING_NONE', 'CODEC_ID_IAC', 'frexpf',
           'AVFilterPacking', 'tolower', '__gets_chk',
           'AVFMT_FLAG_MP4A_LATM', 'EKEYREVOKED',
           'av_default_get_category', 'AV_ROUND_INF', 'cbrt',
           'AVCOL_SPC_YCGCO', 'LIBSWSCALE_BUILD', '__quad_t',
           'av_samples_alloc', '_BSD_SOURCE', '__obstack_vprintf_chk',
           '__uid_t', 'MATH_ERRNO', 'av_seek_frame', '_SVID_',
           'strverscmp', 'LIBAVFILTER_VERSION_MINOR', 'FF_CMP_PSNR',
           'AV_DISPOSITION_CLEAN_EFFECTS', 'avfilter_register',
           '_IO_USER_BUF', '__USE_LARGEFILE64', 'strtol',
           'CODEC_ID_ADPCM_XA', 'av_compare_mod', 'av_realloc',
           'htobe64', 'CODEC_ID_BFI', 'LIBAVFORMAT_VERSION_MINOR',
           'strtod', 'strtof', 'ME_UMH', 'PIX_FMT_RGB8',
           'AV_CPU_FLAG_SSE2SLOW', 'FF_QSCALE_TYPE_H264',
           'CODEC_ID_DFA', 'PIX_FMT_RGB4', 'PIX_FMT_YUV422P16BE',
           'PIX_FMT_RGB0', 'SwsFilter', '_IO_padn', 'CODEC_ID_DTS',
           'PP_CPU_CAPS_MMX2', 'int_fast8_t', 'av_fast_padded_malloc',
           'PIX_FMT_RGBA', 'NZERO', 'mkstemp', 'bcmp', 'strxfrm_l',
           'erfcl', 'swscale_version', 'memcpy',
           'av_find_default_stream_index', 'av_new_stream',
           'pp_context', 'av_log_format_line',
           'AV_AUDIO_SERVICE_TYPE_HEARING_IMPAIRED', 'MB_TYPE_QUANT',
           'AVResampleContext', 'FF_PROFILE_AAC_MAIN',
           'avfilter_get_audio_buffer_ref_from_arrays', 'EKEYEXPIRED',
           'AV_CH_SIDE_LEFT', '__bos',
           'avfilter_get_video_buffer_ref_from_arrays', 'nextafterl',
           '__ssize_t', 'gid_t', 'nextafterf',
           'program_invocation_name', 'lcong48_r', 'int16_t',
           'PIX_FMT_YUV422P16LE', 'avcodec_find_decoder', 'stpcpy',
           'sws_convertPalette8ToPacked32', '__warnattr',
           'AV_PERM_WRITE', '__sigset_t', 'getdate',
           'CODEC_CAP_DELAY', 'av_pkt_dump2', '__isalnum_l',
           '_POSIX2_BC_DIM_MAX', 'avfilter_default_start_frame',
           'jnl', 'strtold_l', 'scalbln', 'AV_CLASS_CATEGORY_DECODER',
           'ENOSR', 'ilogbl', 'FF_DEBUG_MB_TYPE', 'PP_CPU_CAPS_3DNOW',
           'SWS_CS_SMPTE170M', 'ilogbf', 'MB_TYPE_P1L0',
           'MB_TYPE_P1L1', 'atanhl', 'AVFILTER_PLANAR',
           'FF_LOSS_ALPHA', 'ushort', 'CODEC_ID_PCM_U16LE',
           'clockid_t', '_IO_size_t', 'caddr_t', 'AV_LOG_QUIET',
           'uint16_t', 'strftime', 'pp_get_mode_by_name_and_quality',
           'CODEC_ID_ADPCM_IMA_APC', 'ENXIO', 'ECONNREFUSED',
           'AV_CH_STEREO_LEFT', 'AV_CH_LAYOUT_7POINT0',
           'AV_CH_LAYOUT_7POINT1', 'CODEC_ID_DSICINVIDEO',
           'tmpfile64', 'CODEC_FLAG_GMC', '__USE_MISC', '__intptr_t',
           'avfilter_pad_get_name', '__USE_EXTERN_INLINES_IN_LIBC',
           'getsubopt', 'av_picture_pad', 'CODEC_ID_HUFFYUV',
           'AVFilterPool', 'obstack', 'WIFEXITED', 'FF_IDCT_VP3',
           'PIX_FMT_RGB48BE', 'va_arg', 'av_url_split',
           'av_audio_resample_init', '_IO_2_1_stderr_',
           'AV_SAMPLE_FMT_NONE', 'PIX_FMT_BGR565BE', 'ELIBSCN',
           'LIBAVUTIL_BUILD', 'CODEC_ID_WMAV1', 'av_gettime',
           'CODEC_ID_ADPCM_EA_MAXIS_XA', '_BITS_BYTESWAP_H', 'cos',
           'WSTOPSIG', '__dev_t', '_IO_HAVE_SYS_WAIT',
           'AV_SAMPLE_FMT_DBLP', '_SYS_SYSMACROS_H',
           'av_parser_change', 'drand48', 'truncl', 'av_dict_copy',
           'LIBAVFORMAT_VERSION_MICRO', '__dprintf_chk', 'truncf',
           'PIX_FMT_BGR0', 'lgamma', 'CODEC_ID_PCM_F64LE',
           'clock_gettime', 'lgamma_r', 'j1l', 'vsprintf',
           'av_guess_format', 'log10l', 'av_free_packet',
           '__USE_POSIX199506', 'avfilter_formats_ref',
           'av_close_input_file', '__BIG_ENDIAN', 'srand',
           'uintmax_t', 'EACCES', 'AV_CH_LAYOUT_2_1',
           'AV_CH_LAYOUT_2_2', 'PIX_FMT_YUVJ422P', 'ispunct',
           '_POSIX2_BC_STRING_MAX', 'getc', 'FF_CODER_TYPE_AC',
           'strcasecmp_l', '__fsblkcnt64_t', 'finite',
           'PIX_FMT_BGRA64LE', 'SWS_SRC_V_CHR_DROP_SHIFT',
           'avcodec_get_type', 'av_mul_q',
           'AV_CH_LAYOUT_7POINT1_WIDE_BACK', 'PIX_FMT_ABGR',
           '_G_HAVE_PRINTF_FP', '__ino_t', 'PARSER_FLAG_ONCE',
           'MKBETAG', 'CODEC_FLAG_BITEXACT',
           'avcodec_decode_subtitle2', 'strcoll_l', '__REDIRECT_LDBL',
           'ENODATA', 'avfilter_default_draw_slice', 'AVPictureType',
           'PIX_FMT_YUV420P10LE', 'WCONTINUED', 'drand48_r',
           'AVCOL_PRI_NB', 'log', 'powl', 'powf', 'CODEC_ID_JPEGLS',
           'be16toh', 'avio_printf', 'av_register_output_format',
           '__timezone', '_TIME_H', '__SIZEOF_PTHREAD_BARRIERATTR_T',
           'EDOTDOT', 'av_rescale_q_rnd', 'AVSEEK_SIZE', '__isinfl',
           'CODEC_ID_PCX', 'ESOCKTNOSUPPORT', 'isxdigit_l',
           'AVMEDIA_TYPE_SUBTITLE', 'PIX_FMT_BGRA64BE', '_ISOC_',
           '__stpncpy_chk', 'AVFrame', 'MAX_CANON', 'audio_resample',
           'FF_MAX_B_FRAMES', 'AVAudioServiceType',
           'avcodec_alloc_context3', 'avcodec_alloc_context2',
           'PIX_FMT_NB', 'int32_t', 'IOV_MAX', 'PIX_FMT_NE',
           'CODEC_ID_PICTOR', 'LIBAVCODEC_VERSION_MINOR', '_IO_MAGIC',
           '__vprintf_chk', 'imaxabs', 'AV_CPU_FLAG_FORCE',
           'FF_BUFFER_HINTS_VALID', 'WIFSTOPPED', 'EEXIST',
           'FF_BUFFER_HINTS_PRESERVE', 'avfilter_version',
           'AVPacketList', 'EPROTO', '_SYS_SELECT_H', '__isxdigit_l',
           '_G_fpos64_t', 'avfilter_insert_filter', '_ISOC95_SOURCE',
           'AVFMT_FLAG_DISCARD_CORRUPT', 'timer_create', 'FF_CMP_BIT',
           '__compar_fn_t', 'AV_CLASS_CATEGORY_BITSTREAM_FILTER',
           'modfl', 'FF_PROFILE_MPEG4_SIMPLE_STUDIO',
           'ULONG_LONG_MAX', 'CODEC_ID_ADPCM_THP', '__io_close_fn',
           'AVERROR_EXIT', 'pclose', 'AV_CPU_FLAG_SSE3SLOW', 'llabs',
           'CODEC_ID_TMV', 'av_codec_next', '__clock_t_defined',
           '__codecvt_ok', 'av_demuxer_open', 'MB_TYPE_SKIP',
           'AV_NUM_DATA_POINTERS', '_IO_BAD_SEEN',
           'CODEC_ID_MOV_TEXT', 'fgetc_unlocked', '_IO_UPPERCASE',
           'isxdigit', '_IO_EOF_SEEN', '__sprintf_chk', 'asctime',
           'CODEC_ID_TIERTEXSEQVIDEO',
           'CODEC_CAP_VARIABLE_FRAME_SIZE', 'CLOCK_MONOTONIC',
           'ENOTRECOVERABLE', 'matherr', 'AV_CLASS_CATEGORY_INPUT',
           '__strtoul_internal', 'avfilter_insert_outpad',
           '__stpncpy', 'EINTR', 'EADV', 'INT8_C', 'strlen',
           'AVCOL_RANGE_JPEG', 'sws_convertPalette8ToPacked24',
           'ENOSYS', 'u_int', 'puts', 'SEEK_END', 'av_resample',
           'avfilter_formats_unref', 'sys_errlist', 'strcpy',
           'av_samples_set_silence', 'av_get_bytes_per_sample',
           'av_calloc', 'avfilter_register_all', 'AVCOL_SPC_BT709',
           'avio_wb64', 'FF_IDCT_LIBMPEG2MMX', 'fcvt',
           'CODEC_ID_INDEO3', 'avfilter_poll_frame',
           'CODEC_ID_MPEG1VIDEO', 'uint_least64_t',
           'avcodec_encode_video2', 'CODEC_ID_INTERPLAY_DPCM',
           'isprint', 'avcodec_find_best_pix_fmt', '__USE_UNIX98',
           'fgets_unlocked', '__gid_t', 'PIX_FMT_XVMC_MPEG2_IDCT',
           'CODEC_ID_ADPCM_CT', 'FF_LOSS_COLORSPACE',
           'AV_CH_LAYOUT_5POINT1_BACK', '_IO_OCT', '__daddr_t',
           'AV_CH_LAYOUT_6POINT1_BACK',
           'avcodec_pix_fmt_to_codec_tag', 'url_feof',
           'PARSER_FLAG_FETCHED_OFFSET', 'av_log',
           'CODEC_ID_RAWVIDEO', 'CODEC_ID_ADPCM_MS',
           'CODEC_FLAG2_STRICT_GOP', '__isascii_l', 'u_quad_t',
           'getenv', '__isascii', 'AVCOL_PRI_SMPTE170M',
           'AV_SAMPLE_FMT_S16', 'PIX_FMT_YUV420P9BE', 'SWS_SPLINE',
           'unlockpt', '__wcstoul_internal', 'ME_PHODS', '_IO_getc',
           'AVSubtitleType', '_ISprint', 'cuserid', 'CODEC_ID_AMV',
           'PIX_FMT_YUV422P10LE', 'strspn', '__isnan',
           'FF_PROFILE_H264_HIGH_422_INTRA', 'log1p', 'PIX_FMT_NV21',
           'AV_CH_LAYOUT_3POINT1', 'sscanf',
           'avfilter_null_end_frame', 'strndup', 'CODEC_ID_WMAV2',
           'MB_TYPE_L0L1', 'CODEC_ID_QDMC', 'strtoumax',
           '_G_HAVE_IO_FILE_OPEN', 'jrand48_r',
           '_IO_FLAGS2_USER_WBUF', 'ENETDOWN', 'int64_t',
           'FF_LOSS_DEPTH', 'EXIT_FAILURE', 'AV_EF_BUFFER', 'le64toh',
           'CLOCK_PROCESS_CPUTIME_ID', '__va_copy',
           'avformat_close_input', 'EBADFD', '_IO_MAGIC_MASK',
           'CODEC_ID_KMVC', 'AV_CPU_FLAG_NEON', 'TTY_NAME_MAX',
           'AV_DISPOSITION_ORIGINAL', 'CODEC_ID_PCM_ZORK', 'M_SQRT2',
           'PTHREAD_KEYS_MAX', 'ENOMEDIUM', 'FF_DCT_AUTO',
           'CODEC_ID_TQI', 'FD_SETSIZE', '__codecvt_error', '_IOLBF',
           '__wctomb_chk', 'remainderf', 'FF_IDCT_AUTO', '_toupper',
           'remainderl', 'j0f', 'FF_BUG_QPEL_CHROMA2',
           'av_picture_copy', 'AVCOL_PRI_BT470M',
           'PIX_FMT_YUV444P10LE', '_POSIX2_BC_SCALE_MAX',
           'avpicture_get_size', 'locale_t', '__isinf', 'AVRational',
           'SWS_CS_ITU601', 'swscale_configuration', 'MQ_PRIO_MAX',
           'AVINDEX_KEYFRAME', 'AVERROR_BUG2', 'asinhf', 'sincosl',
           'avio_seek', '_G_int32_t', 'CODEC_ID_QDM2',
           'FF_CODER_TYPE_RAW', 'sincosf', 'asinhl']

# include <gtk/gtk.h>
# include <glade/glade.h>

int main ( int argc , char * argv [])
{
	GladeXML * xml ;
	gtk_init (& argc , & argv );
	xml = glade_xml_new ( "videoeditor.glade" , NULL , NULL );
	glade_xml_signal_autoconnect(xml);
	GtkWindow *window = glade_xml_get_widget( xml , "MainWindow" );
	gtk_widget_show ( window );
	gtk_main ();
	return 0;
}


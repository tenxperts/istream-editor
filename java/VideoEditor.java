import org.gnome.gtk.Gtk;
import org.gnome.glade.Glade;
import org.gnome.glade.XML;
import org.gnome.gtk.Window;
import org.gnome.gdk.EventAny;
import java.io.FileNotFoundException;





public final class VideoEditor {
	public static interface MainWindowListener {}
	public static void main(String args[]) {
		final XML glade;
		final Window MainWindow;
		try {	
			Gtk.init(args);
			glade = Glade.parse("videoeditor.glade", "MainWindow");
			MainWindow = (Window)glade.getWidget("MainWindow");
			MainWindow.connect(new MainWindowListener() {
				public void on_MainWindowDestroy(EventAny event) {
				}
			});
			MainWindow.show();
			Gtk.main();
		}
		catch (FileNotFoundException f) {
		}
	}


	public void on_MainWindow_destroy() {
		System.out.println("recieved destroy event");
	}
}

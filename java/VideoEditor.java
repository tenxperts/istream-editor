import org.gnome.gtk.Gtk;
import org.gnome.glade.Glade;
import org.gnome.glade.XML;
import org.gnome.gtk.Window;
import java.io.FileNotFoundException;


public final class VideoEditor {
	public static void main(String args[]) {
		final XML glade;
		final Window MainWindow;
		try {	
			Gtk.init(args);
			glade = Glade.parse("videoeditor.glade", "MainWindow");
			MainWindow = (Window)glade.getWidget("MainWindow");
			MainWindow.show();
			Gtk.main();
		}
		catch (FileNotFoundException f) {
		}
	}
}

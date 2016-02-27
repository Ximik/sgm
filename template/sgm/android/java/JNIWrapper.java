package %package%;

public class JNIWrapper {
    static {
        System.loadLibrary("app");
    }

    public static native void onSurfaceChanged(int width, int height);

    public static native void onDrawFrame();
}
#include "hook.h"
#include <jni.h>

JNIEXPORT void JNICALL Java_%_package_%_JNIWrapper_onSurfaceChanged(JNIEnv * env, jclass cls, jint width, jint height) {
    hook_surface_changed(width, height);
}

JNIEXPORT void JNICALL Java_%_package_%_JNIWrapper_onDrawFrame(JNIEnv * env, jclass cls) {
    hook_draw_frame();
}
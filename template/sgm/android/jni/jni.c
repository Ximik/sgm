#include "hook.h"
#include <jni.h>

JNIEXPORT void JNICALL Java_%_package_%_JNIWrapper_onSurfaceChanged(JNIEnv* /*env*/, jclass /*cls*/, jint width, jint height) {
    hook_surface_changed(width, height);
}

JNIEXPORT void JNICALL Java_%_package_%_JNIWrapper_onDrawFrame(JNIEnv* /*env*/, jclass /*cls*/) {
    hook_draw_frame();
}

JNIEXPORT void JNICALL Java_%_package_%_JNIWrapper_onPause(JNIEnv* /*env*/, jclass /*cls*/) {
    hook_pause();
}

JNIEXPORT void JNICALL Java_%_package_%_JNIWrapper_onResume(JNIEnv* /*env*/, jclass /*cls*/) {
    hook_resume();
}

JNIEXPORT void JNICALL Java_%_package_%_JNIWrapper_onPointerDown(JNIEnv* /*env*/, jclass /*cls*/, jint id, jint x, jint y) {
    hook_pointer_down(id, x, y);
}

JNIEXPORT void JNICALL Java_%_package_%_JNIWrapper_onPointerUp(JNIEnv* /*env*/, jclass /*cls*/, jint id, jint x, jint y) {
    hook_pointer_up(id, x, y);
}

JNIEXPORT void JNICALL Java_%_package_%_JNIWrapper_onPointerMove(JNIEnv* /*env*/, jclass /*cls*/, jint id, jint x, jint y) {
    hook_pointer_move(id, x, y);
}
LOCAL_PATH := $(call my-dir)
SRC_DIR := ../../../src

include $(CLEAR_VARS)

LOCAL_MODULE    := app
LOCAL_CFLAGS    := -Wall -Wextra
LOCAL_SRC_FILES :=
LOCAL_LDLIBS := -lGLESv2 -llog

include $(BUILD_SHARED_LIBRARY)

#include "hook.h"
#include "../../../src/app.h"

#include <time.h>

int hook_time;
App *app;

int hook_get_time()
{
  struct timeval  now;
  gettimeofday(&now, NULL);
  return (int)(now.tv_sec * 1000 + now.tv_usec / 1000);
}

void hook_surface_changed(int width, int height)
{
    if (app) {
        app->restore();
    } else {
        app = new App(width, height);
    }
    app->glLoad();
    hook_time = hook_get_time();
}

void hook_pause()
{
    app->suspend();
}

void hook_draw_frame()
{
    int time = hook_get_time();
    int dt = time - hook_time;
    hook_time = time;
    app->drawFrame(dt);
}

void hook_pointer_down(int id, int x, int y)
{
    app->pointerDown(id, x, y);
}

void hook_pointer_up(int id, int x, int y)
{
    app->pointerUp(id, x, y);
}

void hook_pointer_move(int id, int x, int y)
{
    app->pointerMove(id, x, y);
}

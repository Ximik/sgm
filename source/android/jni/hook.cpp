#include "hook.h"
#include "../../app.h"

#include <time.h>

unsigned int _time;

unsigned int _get_time()
{
  struct timeval  now;
  gettimeofday(&now, NULL);
  return (unsigned int)(now.tv_sec*1000 + now.tv_usec/1000);
}

void hook_surface_changed(unsigned int w, unsigned int h)
{
    App::init(w, h);
    _time = _get_time();
}

void hook_draw_frame()
{
    unsigned int time = _get_time();
    unsigned int t = time - _time;
    _time = time;
    App::tick(t);
}

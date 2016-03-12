#ifndef APP_H
#define APP_H

#include "inc/l_app.h"

class App : public LApp
{
public:
    App(int width, int height);
    void glLoad();
    void drawFrame(int dt);
};

#endif // APP_H

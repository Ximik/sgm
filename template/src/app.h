#ifndef APP_H
#define APP_H

#include "inc/base_app.h"

class App : public BaseApp
{
public:
    App(int width, int height);
    void glLoad();
    void drawFrame(int dt);
};

#endif // APP_H

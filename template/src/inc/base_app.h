#ifndef BASE_APP_H
#define BASE_APP_H

class BaseApp
{
public:
    void glLoad();
    void drawFrame(int dt);
    void suspend() {};
    void restore() {};
    void pointerDown(int id, int x, int y) {};
    void pointerUp(int id, int x, int y) {};
    void pointerMove(int id, int x, int y) {};
};

#endif // BASE_APP_H

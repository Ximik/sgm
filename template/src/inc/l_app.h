#ifndef L_APP_H
#define L_APP_H

class LApp
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

#endif // L_APP_H

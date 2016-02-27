
SRC_DIR= $(PROJECT_DIR)/src
X11_SRC_DIR= $(PROJECT_DIR)/x11/src
	
CXX= g++
CXXFLAGS= -O2 -pipe
INCPATH= $(SRC_DIR)
LINK= g++
LFLAGS= -lX11 -lGLESv2 -lEGL

all: $(OBJECTS)
	$(LINK) $(LFLAGS) -o $(TARGET) $(OBJECTS)
	
clean:
	rm $(OBJECTS) $(TARGET)

main.o: $(X11_SRC_DIR)/main.cpp
	$(CXX) -c $(CXXFLAGS) $(X11_SRC_DIR)/main.cpp

x11.o: $(X11_SRC_DIR)/x11.cpp
	$(CXX) -c $(CXXFLAGS) $(X11_SRC_DIR)/x11.cpp




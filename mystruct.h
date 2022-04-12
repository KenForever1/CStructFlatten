
#ifndef MYSTRUCT_H
#define MYSTRUCT_H
struct Direction {
    int front;
    int back;
    int left;
    int right;
};
struct Test {
    int xx;
    int yy;
};

struct Pos {
    struct Test test;
    int x;
    int y;
    int z;
};

struct All {
    int name;
    struct Pos pos;
    int gender;
    struct Direction direction;
};

#endif //MYSTRUCT_H

class B {
    int a, b;

public:
    B(int aa = 0, int bb = 0) { a = aa; b = bb; }

    B operator+ (int x) {
        B r;
        r.a = a + x;
        r.b = b + x;
        return r;
    }
};
void main() {
    B x(3, 5), y(8, 4), z1, z2;
    z1 = x + 5;  // A
    z2 = 10 + y; // B
}

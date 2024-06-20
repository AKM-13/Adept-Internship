#include <iostream>
#include <string>

using namespace std;

// Function to compute the CRC
string computeCRC(string input, string polynomial) {
    int n = input.length();
    int m = polynomial.length();

    string dividend = input + string(m - 1, '0');

    for (int i = 0; i <= n - 1; i++) {
        if (dividend[i] == '1') {
            for (int j = 0; j < m; j++) {
                dividend[i + j] = (dividend[i + j] == polynomial[j]) ? '0' : '1';
            }
        }
    }

    return dividend.substr(n, m - 1);
}

int main() {
    string input, polynomial;

    cout << "Enter the input binary string: ";
    cin >> input;
    cout << "Enter the polynomial binary string: ";
    cin >> polynomial;

    string crc = computeCRC(input, polynomial);
    string transmitted = input + crc;

    cout << "The computed CRC is: " << crc << endl;
    cout << "The transmitted message is: " << transmitted << endl;

    return 0;
}

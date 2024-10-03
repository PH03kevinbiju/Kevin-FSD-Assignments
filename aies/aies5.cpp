#include <iostream>
#include <cmath>

using namespace std;

int calculateConflicts(int board[], int N) {
    int conflicts = 0;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (board[i] == board[j] || abs(board[i] - board[j]) == abs(i - j)) {
                conflicts++;
            }
        }
    }
    return conflicts;
}

void printBoard(int board[], int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (board[i] == j)
                cout << "Q ";
            else
                cout << ". ";
        }
        cout << endl;
    }
    cout << endl;
}

void initializeBoard(int board[], int N) {
    for (int i = 0; i < N; i++) {
        board[i] = i % N;
    }
}

void solveNQueens(int N) {
    int* board = new int[N];
    initializeBoard(board, N);

    int currentConflicts = calculateConflicts(board, N);

    while (currentConflicts != 0) {
        int* bestBoard = new int[N];
        int bestConflicts = currentConflicts;

        for (int i = 0; i < N; i++) {
            bestBoard[i] = board[i];
        }

        for (int i = 0; i < N; i++) {
            int originalRow = board[i];

            for (int j = 0; j < N; j++) {
                if (j == originalRow)
                    continue;

                board[i] = j;
                int newConflicts = calculateConflicts(board, N);

                if (newConflicts < bestConflicts) {
                    bestConflicts = newConflicts;
                    for (int k = 0; k < N; k++) {
                        bestBoard[k] = board[k];
                    }
                }
            }

            board[i] = originalRow;
        }

        if (bestConflicts == currentConflicts) {
            for (int i = 0; i < N; i++) {
                board[i] = (board[i] + 1) % N;
            }
        } else {
            for (int i = 0; i < N; i++) {
                board[i] = bestBoard[i];
            }
            currentConflicts = bestConflicts;
        }

        delete[] bestBoard;
    }

    printBoard(board, N);
    delete[] board;
}

int main() {
    int N;
    cout << "Enter the number of queens (or size of the board): ";
    cin >> N;

    if (N < 4) {
        cout << "The N-Queens problem has no solutions for N < 4." << endl;
        return 0;
    }

    cout << "Solving " << N << "-Queens Problem using Hill Climbing..." << endl;
    solveNQueens(N);

    return 0;
}

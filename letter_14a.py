def main():
    n, m = map(int, input().split())
    drawing = []
    
    start_row, end_row = n, 0
    start_col, end_col = m, 0

    for row in range(n):
        line = input().strip()
        drawing.append(line)

        for col in range(m):
            if line[col] == '*':
                if row < start_row:
                    start_row = row
                if row > end_row:
                    end_row = row
                if col < start_col:
                    start_col = col
                if col > end_col:
                    end_col = col

    for row in range(start_row, end_row + 1):
        print(drawing[row][start_col:end_col + 1])

if __name__ == "__main__":
    main()

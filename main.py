def queens(n):
  """
  在 nxn 棋盤上放置 n 個皇后。

  Args:
    n: 棋盤的大小。

  Returns:
    所有可能的解。
  """

  def valid(queens, row, col):
    """
    檢查新放置的皇后是否與其他皇后衝突。

    Args:
      queens: 皇后的位置列表。
      row: 新放置皇后的行。
      col: 新放置皇后的列。

    Returns:
      如果不衝突，返回 True；否則，返回 False。
    """
    for r, c in queens:
      if r == row or c == col or abs(row - r) == abs(c - col):
        return False
    return True

  queens = []
  def dfs(queens, row):
    if row == n:
      return queens
    for col in range(n):
      if valid(queens, row, col):
        queens.append((row, col))
        res = dfs(queens, row + 1)
        if res is not None:
          return res
        queens.pop()
  return dfs(queens, 0)

print(queens(8))

#有使用Bard
defmodule Day02Test do
  use ExUnit.Case

  import ElfComputer

  @input [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,5,119,0,99,2,0,14,0]

  test "examples" do
    assert 2 == result([1,0,0,0,99])
    assert 9801 == result([2,4,4,0,99,0])
    assert 30 == result([1,1,1,4,99,5,6,0,99])
  end

  test "part 1" do
    IO.inspect("Day 02, part 1 = " <> to_string(result(initialize(@input, [{1, 12}, {2, 2}]))))
  end

  test "part 2" do
    for n <- 0..99,
      v <- 0..99,
      result(initialize(@input, [{1, n}, {2, v}])) == 19690720,
      do: IO.inspect("Day 02, part 2 = " <> to_string(n * 100 + v))
  end
end
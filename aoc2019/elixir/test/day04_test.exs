defmodule Day04Test do
  use ExUnit.Case

  test "digits never decrease" do
    assert never_decreases(111111)
    refute never_decreases(223450)
  end

  test "doubles" do
    assert doubles(111111)
    assert doubles(223450)
    refute doubles(123789)
  end

  test "part 1" do
    IO.inspect("Day 04, part 1 = " <> to_string(Enum.count(353096..843212, &valid/1)))
  end

  test "part 2" do
    IO.inspect("Day 04, part 2 = " <> to_string(Enum.count(353096..843212, &valid2/1)))
  end

  def valid(n), do: never_decreases(n) and doubles(n)
  def valid2(n), do: never_decreases(n) and only_doubles(n)

  def never_decreases(n) do
    ds = Integer.digits(n)

    ds == Enum.sort(ds)
  end

  def doubles(n) do
    n
    |> Integer.digits()
    |> run_length_encode()
    |> Enum.any?(fn {_, c} -> c >= 2 end)
  end

  def only_doubles(n) do
    n
    |> Integer.digits()
    |> run_length_encode()
    |> Enum.any?(fn {_, c} -> c == 2 end)
  end

  def run_length_encode(ns) do
    ns 
    |> Enum.reduce([], &run_length_encode/2)
  end

  def run_length_encode(n, [{n, c} | rest]), do: [{n, c+1} | rest]
  def run_length_encode(n, rest), do: [{n, 1} | rest]
end
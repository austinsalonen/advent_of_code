defmodule Day01Test do
  use ExUnit.Case

  @input [106985, 113927, 107457, 106171, 69124, 59906, 66420, 149336, 73783, 120127, 139486, 108698, 104091, 103032, 108609, 136293, 144735, 55381, 98823, 103981, 140684, 114482, 133925, 111247, 110833, 92252, 87396, 79730, 61395, 82572, 72403, 140763, 57088, 63457, 65523, 50148, 134758, 93447, 85513, 132927, 139159, 141579, 94444, 56997, 137128, 107930, 67607, 108837, 120206, 79441, 99839, 137404, 140502, 67274, 108736, 97302, 76561, 107804, 134306, 52820, 89632, 101473, 65001, 57399, 82858, 60577, 82043, 144783, 101606, 138900, 68246, 118774, 129919, 99394, 80009, 107404, 121503, 119232, 108157, 117965, 112025, 139205, 126336, 143985, 58894, 93020, 136732, 100535, 144090, 134414, 109049, 105714, 111654, 50677, 77622, 53398, 133851, 71166, 115935, 94067]

  test "required fuel" do
    assert 2 == required_fuel(12)
    assert 2 == required_fuel(14)
    assert 654 == required_fuel(1969)
    assert 33583 == required_fuel(100756)
  end

  test "no negative fuel" do
    assert 0 == required_fuel(2)
  end

  test "fuel for fuel" do
    assert 50346 == fuel_for_fuel(100756)
  end

  test "part 1" do
    Enum.map(@input, &required_fuel/1) 
    |> Enum.sum()
    |> print("Day 01, part 1 = ")
  end

  test "part 2" do
    Enum.map(@input, &fuel_for_fuel/1)
    |> Enum.sum()
    |> print("Day 01, part 2 = ")
  end

  def print(x, prefix) do
    IO.inspect(prefix <> to_string(x))
  end

  def sub2(a), do: a - 2

  def required_fuel(mass) do
    mass |> div(3) |> sub2() |> max(0)
  end

  def fuel_for_fuel(mass) do
    case required_fuel(mass) do
      n when n > 0 -> n + fuel_for_fuel(n)
      _ -> 0
    end
  end
end
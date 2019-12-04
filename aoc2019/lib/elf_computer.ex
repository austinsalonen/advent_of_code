defmodule ElfComputer do
  def initialize(intcode, overrides) do
    overrides
    |> Enum.reduce(intcode, fn {idx, v}, xs -> List.replace_at(xs, idx, v) end)
  end

  def result(intcode) do
    run(intcode, 0)
    |> hd()
  end

  def run(intcode, ptr) do
    case step(intcode, ptr) do
      {:halt, intcode} -> intcode
      {ptr, intcode} -> run(intcode, ptr)
    end
  end

  def step(intcode, ptr) do
    case Enum.at(intcode, ptr) do
      1 -> {ptr + 4, add(intcode, ptr + 1, ptr + 2, ptr + 3)}
      2 -> {ptr + 4, mul(intcode, ptr + 1, ptr + 2, ptr + 3)}
      99 -> {:halt, intcode}
    end
  end

  def add(buffer, ptr_a, ptr_b, dst) do
    List.replace_at(buffer, Enum.at(buffer, dst), Enum.at(buffer, Enum.at(buffer, ptr_a)) + Enum.at(buffer, Enum.at(buffer, ptr_b)))
  end

  def mul(buffer, ptr_a, ptr_b, dst) do
    List.replace_at(buffer, Enum.at(buffer, dst), Enum.at(buffer, Enum.at(buffer, ptr_a)) * Enum.at(buffer, Enum.at(buffer, ptr_b)))
  end
end
defmodule ElfComputer do
  def initialize(intcode, overrides) do
    overrides
    |> Enum.reduce(intcode, fn {idx, v}, xs -> List.replace_at(xs, idx, v) end)
  end

  def result(intcode) do
    run(intcode, 0)
    |> hd()
  end

  def run(intcode, ptr), do: run(intcode, ptr, [])

  def run(intcode, ptr, inputs) do
    case step(intcode, ptr, inputs) do
      {:halt, intcode, _} -> intcode
      {ptr, intcode, xs} -> run(intcode, ptr, xs)
    end
  end

  def step(intcode, ptr, inputs) do
    case Enum.at(intcode, ptr) do
      1 -> {ptr + 4, add000(intcode, ptr + 1, ptr + 2, ptr + 3), inputs}
      2 -> {ptr + 4, mul000(intcode, ptr + 1, ptr + 2, ptr + 3), inputs}
    102 -> {ptr + 4, mul100(intcode, ptr + 1, ptr + 2, ptr + 3), inputs}
    1002 -> {ptr + 4, mul010(intcode, ptr + 1, ptr + 2, ptr + 3), inputs}
      3 -> {ptr + 2, put(intcode, ptr + 1, hd(inputs)), tl(inputs)}
      4 -> {ptr + 2, write(intcode, ptr + 1), inputs}
      99 -> {:halt, intcode}
    end
  end

  def add000(buffer, ptr_a, ptr_b, dst) do
    List.replace_at(buffer, Enum.at(buffer, dst), Enum.at(buffer, Enum.at(buffer, ptr_a)) + Enum.at(buffer, Enum.at(buffer, ptr_b)))
  end

  def mul000(buffer, ptr_a, ptr_b, dst) do
    List.replace_at(buffer, Enum.at(buffer, dst), Enum.at(buffer, Enum.at(buffer, ptr_a)) * Enum.at(buffer, Enum.at(buffer, ptr_b)))
  end

  def mul100(buffer, ptr_a, ptr_b, dst) do
    List.replace_at(buffer, Enum.at(buffer, dst), Enum.at(buffer, ptr_a) * Enum.at(buffer, Enum.at(buffer, ptr_b)))
  end

  def mul010(buffer, ptr_a, ptr_b, dst) do
    List.replace_at(buffer, Enum.at(buffer, dst), Enum.at(buffer, Enum.at(buffer, ptr_a)) * Enum.at(buffer, ptr_b))
  end

  def put(buffer, ptr, val) do
    List.replace_at(buffer, Enum.at(buffer, ptr), val)
  end

  def write(buffer, ptr) do
    require Logger
    # IO.inspect({buffer, ptr, })
    Logger.info("Writing... " <> to_string(Enum.at(buffer, Enum.at(buffer, ptr))))
    buffer
  end
end
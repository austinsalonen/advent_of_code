defmodule Day05Test do
  use ExUnit.Case
  import ExUnit.CaptureLog

  import ElfComputer

  test "opcode 3" do
    assert {2, [1, 0, 99], []} == step([3, 0, 99], 0, [1])
  end

  test "opcode 4" do
    f = fn -> 
      assert {2, [4, 0, 99], []} == step([4, 0, 99], 0, [])
    end

    assert capture_log(f) =~ "Writing... 4"
  end

  test "modes" do
    assert {4, [102,3,4,4,99], []} == step([102,3,4,4,33], 0, [])
    assert {4, [1002,4,3,4,99], []} == step([1002,4,3,4,33], 0, [])
  end
end
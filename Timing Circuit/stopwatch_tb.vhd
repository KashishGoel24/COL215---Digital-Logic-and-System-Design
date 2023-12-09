----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 10/28/2022 12:08:17 PM
-- Design Name: 
-- Module Name: stopwatch_tb - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity stopwatch_tb is
--  Port ( );
end stopwatch_tb;

architecture Behavioral of stopwatch_tb is

component stopwatch 
Port (clk : in std_logic;
          start : in std_logic;
          pause : in std_logic;
          continue : in std_logic;
          reset : in std_logic;
          
          
          
          dp : out std_logic;
          cat : out std_logic_vector(6 downto 0);
          an : out std_logic_vector(3 downto 0) );


end component;
signal clock : std_logic;
signal strt: std_logic;
signal paus: std_logic;
signal cont: std_logic;
signal rest: std_logic;
signal deci: std_logic;
signal cathode:std_logic_vector(6 downto 0);
signal anode : std_logic_vector(3 downto 0);
begin

process 
begin
clock<='0';
wait for 5 ns;
clock<='1';
wait for 5 ns;
end process;

strt<='0','1' after 50 ns;
paus<='0','1' after 20 ms,'0' after 40 ms;
cont<='0' ,'1' after 40 ms;
rest<='0','1' after 60 ms; 
UUT : stopwatch port map(clk=>clock,start=>strt,pause=>paus,continue=>cont,reset=>rest,dp=>deci,cat=>cathode,an=>anode);






end Behavioral;
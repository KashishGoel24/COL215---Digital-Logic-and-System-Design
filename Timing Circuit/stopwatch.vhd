 ----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 10/26/2022 12:59:16 PM
-- Design Name: 
-- Module Name: stopwatch - Behavioral
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
use ieee.std_logic_unsigned.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity stopwatch is
    Port (clk : in std_logic;
          start : in std_logic;
          pause : in std_logic;
          continue : in std_logic;
          reset : in std_logic;
          
          
          
          dp : out std_logic;
          cat : out std_logic_vector(6 downto 0);
          an : out std_logic_vector(3 downto 0) );
end stopwatch;

 architecture Behavioral of stopwatch is
component
time_ckt is
  Port (dig3,dig2,dig1,dig0 : in std_logic_vector(3 downto 0);
        cat : out std_logic_vector(6 downto 0 );
        an : out std_logic_vector(3 downto 0 );
        clk : in std_logic ;
        dp : out std_logic);
end component;
signal mm, s1,s2,ms : std_logic_vector(3 downto 0) := "0000";
signal a : integer := 0 ;
signal x : std_logic;
signal ms_clock : std_logic;
signal enable_watch : std_logic :='0';
signal y,z,w : std_logic;
signal reset_watch : std_logic:='1';
signal start_prev : std_logic;
signal pause_prev : std_logic;
signal continue_prev : std_logic;
signal reset_prev : std_logic;
begin

--process(start)
--begin
--if rising_edge(start) then 
--    enable_watch<='1';
--    reset_watch<='0';
--    end if;
--end process;
--process(pause)
--begin 
    
--if rising_edge(pause) then 
--    enable_watch<='0';
--    end if;
--end process;
--process(continue)
--begin

--if rising_edge(continue) then
--    if reset_watch = '0' then 
--        enable_watch<='1';
--    end if;
--end if;
--end process;
--process(reset)
--begin 
--if rising_edge(reset) then 
--    enable_watch<='0';
--    reset_watch<='1';
--    mm<="0000";
--    s1<="0000";
--    s2<="0000";
--    ms<="0000";

    
    
--end if;
--end process;


process(start,pause,continue,reset)
begin 
if reset='1' then 
    reset_watch<='1';
    enable_watch<='0';
        
    
    
    else
    if start='1' then 
        if(pause = '1') then
        
        enable_watch<='0';
        elsif( reset_watch='0' and enable_watch='0' and continue='1') then
        enable_watch<='1';        
        else 
        enable_watch<='1';
        reset_watch<='0';
        
        end if;
    else
        if(pause = '1') then
        
        enable_watch<='0';
        elsif( reset_watch='0' and enable_watch='0' and continue='1') then
        enable_watch<='1';
        end if;
    
    
    
    
    
    end if;
    
    
    
    end if;


end process;






--process(start_prev,pause_prev,continue_prev,reset_prev)
--begin 
--if (rising_edge(start_prev)) then 
--    enable_watch<='1';
--    reset_watch<='0';
    
--elsif rising_edge(pause_prev) then 
--    enable_watch<='0';
    
--elsif rising_edge(continue_prev) then 
--    if( reset_watch = '0') then
--        enable_watch<='1';
--    end if;

--elsif rising_edge(reset_prev) then 
--    enable_watch<='0';
--    reset_watch<='1';
--    end if;

--end process;
















process(clk,reset_watch,enable_watch)
begin
 
if( reset_watch='0' and enable_watch='1') then 
if rising_edge(clk) then
    
        if( a = 10000000) then 
            a <=0;
        else 
            a<=a+1;
        end if;
end if;
end if;
end process;





process(a) 
begin 
if (a = 10000000) then
    x<='0';
else
    x<='1';
end if;
end process;


process(x)
begin
if(reset_watch = '1') then
ms<="0000";
else

if(rising_edge(x)) then 
    if( ms = "1001") then 
        ms<="0000";
    else 
        ms<=ms+'1';
    end if;

end if;
end if;
end process;








process(ms)
begin
if(ms = "1001") then 
    y<='0';
else
y<='1';
end if;
end process;






process(y)
begin
if reset_watch='1' then 
s2<="0000";
else
if(rising_edge(y)) then 
    if(s2 = "1001") then
        s2<="0000";
    else 
        s2<=s2+'1';
    end if;
    end if;
    
    end if;
end process;






process(s2)
begin
if(s2 = "1001") then 
    z<='0';
else
z<='1';
end if;
end process;







process(z)
begin

if reset_watch='1' then 
s1<="0000";
else

if(rising_edge(z)) then 
    if(s1="0101") then 
        s1<="0000";
    else
        s1<=s1+'1';
    end if;
    end if;
    
end if;
end process;







process(s1)
begin
if(s1 = "0101") then 
    w<='0';
else
w<='1';
end if;
end process;











process(w)
begin

if reset_watch='1' then 
mm<="0000";
else

if(rising_edge(w)) then 
    if (mm = "1001") then 
    mm<="0000";
    else
    mm<=mm+'1';
    end if;
    end if;


end if;

end process;






U1 : time_ckt port map (dig3=>mm,dig2=>s1,dig1=>s2,dig0=>ms,cat=>cat ,an=>an, clk=>clk,dp=>dp);


end Behavioral;

"""
Filename: television.py
Author: Talieisn Reese
Version: 1.3
Date: 11/11/2023
Purpose: Go outside
"""
class Television:
  """
  A class that represents a television. Far less interesting than the real thing.
  """
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3
  def __init__(self)-> None:
    """ If you want a Television, you must first BEND REALITY TO YOUR WHIMS AND CREATE IT EX NIHILO"""
    self.__status = False
    self.__muted = False
    self.__volume = Television.MIN_VOLUME
    self.__channel = Television.MIN_CHANNEL
  def power(self)-> None:
    """Turn the TV off or on."""
    if self.__status:
      self.__status = False
    else:
      self.__status = True
  def mute(self)-> None:
    """Stop the volume. Only works if TV is ON"""
    if self.__status == True:
      if self.__muted:
        self.__muted = False
      else:
        self.__muted = True
  def channel_up(self)-> None:
    """Iterate channel up by one. If channel is at maximum, loop back to minimum. Only works if TV is ON"""
    if self.__status == True:
      if self.__channel == Television.MAX_CHANNEL:
        self.__channel = Television.MIN_CHANNEL
      else:
        self.__channel += 1
  def channel_down(self)-> None:
    """Iterate channel down by one. If channel is at minimum, loop back to maximum. Only works if TV is ON"""
    if self.__status == True:
      if self.__channel == Television.MIN_CHANNEL:
        self.__channel = Television.MAX_CHANNEL
      else:
        self.__channel -= 1
  def volume_up(self)-> None:
    """Iterate volume up by one. If volume is at maximum, don't iterate any longer. Automatically un-mutes the TV. Only works if TV is ON"""
    if self.__status == True:
      if self.__volume < Television.MAX_VOLUME:
        self.__volume += 1
        self.__muted = False
  def volume_down(self)-> None:
    """Iterate volume down by one. If volume is at minimum, don't iterate any longer. Automatically un-mutes the TV. Only works if TV is ON"""
    if self.__status == True:
      if self.__volume > Television.MIN_VOLUME:
        self.__volume -= 1
        self.__muted = False
  def __str__(self)-> str:
    """
    Display stats of the TV
    :returns: string: the TV's statistics, formatted as a string."""
    if self.__muted == False:
      return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
    else:
      return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {0}"

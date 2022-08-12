from classes import *
import pytest

class TestClass:
     
     def setup_method(self):
         self.tv = Television() 
     
     def teardown_method(self):
         del self.tv
         
     def test___init__(self):
         #checks the default settings/ str method
         assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
     
     def test_power(self):
         self.tv.power()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
         self.tv.power()
         assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
         
     def test_channel_up(self):
         #Checking that the channel doesn't increment while off
         self.tv.channel_up()
         assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
         
         #Checking if channel increments while on
         self.tv.power()
         self.tv.channel_up()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
         self.tv.channel_up()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
         self.tv.channel_up()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
         
         #Checking if the channel cycles through
         self.tv.channel_up()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
         
     def test_channel_down(self):
         #Checking that the channel doesn't increment while off
         self.tv.channel_down()
         assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
         
         #Checking if the channel cycles through
         self.tv.power()
         self.tv.channel_down()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
         
         
         #Checking if channel increments while on
         self.tv.channel_down()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
         self.tv.channel_down()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
         self.tv.channel_down()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
         
       
     def test_volume_up(self):
         
         #checking that the volume doesn't increment while Tv is off
         self.tv.volume_up()
         assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
         
         #Checking volume increments up 1 while Tv is on
         self.tv.power()
         self.tv.volume_up()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
         self.tv.volume_up()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'         
         
         #checking that the volume cannot exceed maximum
         self.tv.volume_up()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
         
         
     def test_volume_up(self):
         
         #checking that the volume doesn't increment while Tv is off
         self.tv.volume_down()
         assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
         
          #checking that the volume cannot exceed minimum
         self.tv.power() 
         self.tv.volume_down()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

         #Checking volume increments down 1 while Tv is on

         self.tv.volume_up()# placing volume at 2 for testing
         self.tv.volume_up()
         
         self.tv.volume_down()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
         self.tv.volume_down()
         assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'         
         

         
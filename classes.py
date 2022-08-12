class Television:
    '''
    The Television class is responsible for outlining the controls for this particular television. 
    '''
    
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        '''
        Constructor method.
        Sets the volume, and channel and the T.V to off by default.
        '''
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self) -> None:
        '''
        This method changes the state of the television from on to off, and vice versa.
        '''
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def channel_up(self) -> None:
        '''
        This method increments the channel up by 1.
        with the exception if the the channel limit is reached,
        where it cycle back to channel 0.
        if the tv is on
        '''
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        This method increments the channel down by 1.
        with the exception if the the channel limit is reached,
        where it cycle back to channel 3.
        if the tv is on
        '''
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        '''
        This method increments the volume up by 1, as long as the maximum volume has not been achieved.
        if the tv is on
        '''
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume +=1

    def volume_down(self) -> None:
        '''
        This method increments the volume down by 1, as long as the minimum volume has not been achieved.
        if the tv is on
        '''
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
       
    def __str__(self) -> str:
        '''
        This method returns all the relevant information for the TV state, including volume, channel, and whether its on.
        '''
        response = f'TV status: Is on = {str(self.__status)}, Channel = {self.__channel}, Volume = {self.__volume}'
        return response
        
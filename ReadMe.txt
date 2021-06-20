The old script checked to see if Cardano's price was above or below two values then sent different emails based on that. 

The newer CardanoReport,  gets the price and todays tweets that mention cardano, if the user is verrified. 
It also removes links cause I dont need all kinds of rado links emailed to me daily that I could accidently click.  
Use's Twint, if you want to set this up take a look at Network chucks youtube video. https://www.youtube.com/watch?v=SvO_FDa8AIs  

Or you could read the documentation. 
https://github.com/twintproject/twint/wiki

On Windows I set this up to run with task scheduler and on Linux its a CronJob. 

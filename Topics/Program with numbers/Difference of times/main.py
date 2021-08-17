# put your python code here
hours_went_for_a_walk = int(input())
minutes_went_for_a_walk = int(input())
seconds_went_for_a_walk = int(input())

hours_when_it_started_raining = int(input())
minutes_when_it_started_raining = int(input())
seconds_when_it_started_raining = int(input())

hours_into_seconds_went_for_a_walk = (hours_went_for_a_walk * 3600)
minutes_seconds_went_for_a_walk = (minutes_went_for_a_walk * 60)
seconds_went_for_a_walk = seconds_went_for_a_walk
total_seconds_went_for_a_walk = ((hours_went_for_a_walk * 3600) + (minutes_went_for_a_walk * 60) + seconds_went_for_a_walk)

hours_into_seconds_when_it_started_raining = (hours_when_it_started_raining * 3600)
minutes_seconds_when_it_started_raining = (minutes_when_it_started_raining * 60)
seconds_when_it_started_raining = seconds_when_it_started_raining

total_seconds_when_it_started_raining = ((hours_when_it_started_raining * 3600) + (minutes_when_it_started_raining * 60) + seconds_when_it_started_raining)

difference = (total_seconds_when_it_started_raining - total_seconds_went_for_a_walk)

print(difference)

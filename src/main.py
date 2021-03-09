from utility import hashWithAllMethods
import time

start, times = time.perf_counter(), {}

testString = b"Obi-Wan Kenobi: It's over Anakin, I have the high ground. ... Obi-Wan Kenobi: YOU WERE THE CHOSEN ONE! It was said that you would destroy the Sith, not join them, bring balance to the force, not leave it in darkness. Anakin Skywalker/Darth Vader: I HATE YOU!"

hashWithAllMethods(testString)
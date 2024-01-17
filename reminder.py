import time

def set_reminder(reminder_time):
    current_time = time.time()
    aizkave_sekundes = reminder_time - current_time

    if aizkave_sekundes > 0:
        print(f"Atgādinājums iestatīts uz {reminder_time}")
        time.sleep(aizkave_sekundes)
        print("Atgādinājums: Laiks veikt uzdevumu!")
    else:
        print("Nederīgs atgādinājuma laiks. Lūdzu, iestatiet nākotnes laiku.")
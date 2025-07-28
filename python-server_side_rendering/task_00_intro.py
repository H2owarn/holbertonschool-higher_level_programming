import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: Attendees must be a list of dictionaries.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        try:
            personalized = template
            for key in ["name", "event_title", "event_date", "event_location"]:
                value = attendee.get(key)
                personalized = personalized.replace(f"{{{key}}}", value if value else "N/A")

            with open(f"output_{i}.txt", "w") as f:
                f.write(personalized)

        except Exception as e:
            print(f"Error processing attendee {i}: {e}")

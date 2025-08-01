from agents import perception, mobility, manipulation, task_planning, interaction

def main():
    interaction.generate_speech("Hello, I am JetRover. How can I help you?")
    while True:
        command = interaction.listen_for_command()
        if not command:
            continue

        parsed_command = task_planning.interpret_command(command)

        if not parsed_command:
            interaction.generate_speech("I'm sorry, I had trouble understanding that.")
            continue

        intent = parsed_command.get('intent')
        entities = parsed_command.get('entities', {})

        if intent == 'detect_object':
            perception.detect_object(entities.get('object_name', 'an object'))
        elif intent == 'track_object':
            perception.track_object(entities.get('object_name', 'an object'))
        elif intent == 'describe_scene':
            perception.describe_scene()
        elif intent == 'detect_obstacle':
            perception.detect_obstacle()
        elif intent == 'move_to_location':
            mobility.move_to_location(entities.get('location', 'a location'))
        elif intent == 'follow_line':
            mobility.follow_line()
        elif intent == 'return_to_start':
            mobility.return_to_start()
        elif intent == 'precision_movement':
            mobility.precision_movement(entities.get('movement', 'a movement'))
        elif intent == 'pick_and_place':
            manipulation.pick_and_place(entities.get('item', 'an item'))
        elif intent == 'sort_blocks':
            manipulation.sort_blocks(entities.get('color', 'a color'))
        elif intent == 'exit':
            interaction.generate_speech("Goodbye!")
            break
        else:
            interaction.generate_speech("I'm sorry, I don't know how to do that.")

if __name__ == "__main__":
    main()
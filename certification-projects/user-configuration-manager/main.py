#Define the dictionary
test_settings = {
    'theme': 'light',
    'volume': 'high'
}

# Define the function add_setting
def add_setting(test_settings, setting):
    key, value = setting

    # Convert the key and value to lowercase
    key = key.lower()
    value = value.lower()

    # Check if the key setting exists
    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    test_settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

# Define the function update_setting
def update_setting(test_settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    # Check if the key exists
    if key in test_settings:
        test_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# Define the function delete_setting
def delete_setting(test_settings, key):
    key = key.lower()

    # Check if the key exists
    if key in test_settings:
        del test_settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


# Define the function view_settings
def view_settings(test_settings):
    if not bool(test_settings):
        return "No settings available."

    result = "Current User Settings:\n"
    for key, value in test_settings.items():
        result += f"{key.capitalize()}: {value}\n"
        
    return result





print(add_setting(test_settings, ('Notifications', 'enabled')))

print(view_settings(test_settings))
    

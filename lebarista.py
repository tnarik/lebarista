CONFIG_FILE_PATHS = ['~/.lebarista.yaml', '.lebarista.yaml']

# An empty function to use when configuration or dependencies are missing (as this is not a vital piece)
def notify(text):
  pass
        
try:
  from slackclient import SlackClient
  import yaml
  import os
  

  for config_file in CONFIG_FILE_PATHS:
    if os.path.exists(os.path.expanduser(config_file)):
      break

  if os.path.exists(os.path.expanduser(config_file)):
    with open(os.path.expanduser(config_file), 'r') as file:
      config = yaml.load(file)

    try:
      slack_notifier = SlackClient(config['slack']['token'])
      
      def notify(text):
        slack_notifier.api_call(
          "chat.postMessage",
          channel=config['slack']['channel'],
          text=text
      );
    except:
      del config
      print('No configuration data available')
      print("Configure a '{}' file to enable notifications".format(config_file))
      print("You can use '{}' as an example".format('https://github.com/tnarik/lebarista/blob/master/lebarista.yaml.example'))
    finally:
      del file
  else:
    config_file = None
    print('No configuration file available')
    print("Create a '{}' file to enable notifications".format('.lebarista.yaml'))
    print("You can use '{}' as an example".format('https://github.com/tnarik/lebarista/blob/master/lebarista.yaml.example'))
except (ModuleNotFoundError, ImportError):
  print("There won't be any notifications triggered as dependencies are missing. Please reinstall.")

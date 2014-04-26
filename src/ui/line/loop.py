__author__ = 'rburke'

running = 1

def quit_fn (cmd_words):
    global running
    print "Quitting PandaPrepared"
    running = 0

def reset_fn (cmd_words):
    print "Command not implemented: $", cmd_words

def survey_fn (cmd_words):
    print "Command not implemented: $", cmd_words

def notify_fn (cmd_words):
    print "Command not implemented: $", cmd_words

def list_fn (cmd_words):
    print "Command not implemented: $", cmd_words

dispatchDictionary = { 'quit' : quit_fn, 'q' : quit_fn,
                      'exit' : quit_fn, 'x' : quit_fn,
                      'reset' : reset_fn,
                      'survey' : survey_fn,
                      'notify' : notify_fn,
                      'list' : list_fn }

def loop ():
    while (running == 1):
        cmd = raw_input('PPREP> ')
        cmd_words = cmd.split()
        command = cmd_words[0]
        if (command in dispatchDictionary):
            dispatch_fn = dispatchDictionary[command]
            dispatch_fn(cmd_words)
        else:
            print "Command $ not recognized.", command

if __name__ == '__main__':
    loop()

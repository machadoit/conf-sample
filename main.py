#!/usr/bin/env python2

# SHOULD trigger 'Line too long'
# SHOULD trigger 'Invalid constant name'
this_is_an_intentionally_long_name_to_trigger_a_line_too_long_message_from_pylint = None

# SHOULD trigger 'Using a conditional statement with a constant value'
# SHOULD NOT trigger 'More than one statement on a single line'
if True: pass

while True:
  # SHOULD NOT trigger 'Bad indentation'
  break # 2 space indent

while True:
    # SHOULD trigger 'Bad indentation'
    break # 4 space indent

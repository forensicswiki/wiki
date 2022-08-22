**Short Message Service** (**SMS**) is a service that [digital
phones](cell_phones "wikilink") can use to send short messages between
phones. SMS messages are more commonly called text messages, and very
popular among today's youth.

## History

SMS was originally designed for [GSM](GSM "wikilink"), but most all of
the large digital mobile phone providers provide the ability to send
messages to other phones via the SMS.

## Popularity

## Forensics Standpoint

Most modern phones store the SMS in their internal memory, rather than
on the SIM card; in this case forensics should target the phone itself.
If the phone does not store the SMS on the SIM card, it can be
reconfigured to do so (whether this is possible and how it is done
depends on the phone brand and model).

If the phone stores the SMS on the SIM card, forensics should target the
card; there is a chance to recover a deleted SMS.

This is possible because some phones will only mark the SMS as deleted
(instead of overwriting it with 0 or 1 bits); the text of the SMS will
continue to reside on the card until a new SMS is received and the space
will be overwritten with the contents of the new message.

## SMS Recovery Tools

- [pySIM](http://twhiteman.netfirms.com/pySIM.html), a "SIM card
  management tool, capable of creating, editing, deleting, backup and
  restore operations on your SIM Phonebook and SMS records."
- [adafruit industries](http://www.adafruit.com/category/27) has a
  low-cost SIM reader kit that you can get from their website.

## External Links

- [An entry level tutorial that explains the details behind the SMS
  recovery
  process](http://www.dekart.com/howto/howto_sim_reader/how_to_recover_a_deleted_sms/)
- [A video tutorial that shows how an SMS can be
  recovered](http://www.youtube.com/watch?v=VaBaqZiNW4U) (but does not
  go into the low-level details of the process)
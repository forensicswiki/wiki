Zeitgeist is a service which logs the users's activities and events,
anywhere from files opened to websites visited and conversations.

## activity.sqlite

    $HOME/.local/share/zeitgeist/activity.sqlite

event_view seems one of the more interesting tables (which is
technically a view and not a table).

The timestamp is formatter in milli seconds sinds POSIX epoch (Jan 1,
1970 00:00:00 UTC)

    SELECT datetime((timestamp/1000), "unixepoch"), subj_uri, subj_origin_uri, subj_text, subj_storage, event_origin_uri, actor_uri FROM event_view;

## External Links

- [Zeitgeist Project site](http://zeitgeist-project.com/)
- [Wikipedia: Zeitgeist
  (framework)](http://en.wikipedia.org/wiki/Zeitgeist_(framework))

[Category:Applications](Category:Applications "wikilink")
[Category:Linux](Category:Linux "wikilink")
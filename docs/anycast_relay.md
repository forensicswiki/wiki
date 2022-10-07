---
tags:
  -  Articles that need to be expanded 
---
The AnyCast-relay is a core component of the [Open Computer Forensics
Architecture](open_computer_forensics_architecture.md)
for communicating tasks or jobs between processes. Build upon the
concept of an on-disk persistent priority queue, the AnyCast-relay
implements a a collection of named multi-producer multi-consumer work
queues for modules in the Open Computer Forensics Architecture. In OCFA,
a process identifies itself to the AnyCast-relay as being an instance of
a named type of module and in doing so registers itself with the AnyCast
as worker for that module. The name of the AnyCast relay stems from the
fact that the produces creates and forwards a job that is than delivered
to **any** worker registered as instance of the named module. The
AnyCast-relay uses a limited set of static message priorities to sort
the jobs that age given to the workers.

In modern terminology the AnyCast-relay should probably be clasified as
a message bus.
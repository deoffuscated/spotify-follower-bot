import base64, codecs
magic = 'DQoNCnRyeToNCiAgICBpbXBvcnQgcmVxdWVzdHMsIHJhbmRvbSwgc3RyaW5nDQpleGNlcHQgSW1wb3J0RXJyb3I6DQogICAgaW5wdXQoIkVycm9yIHdoaWxlIGltcG9ydGluZyBtb2R1bGVzLiBQbGVhc2UgaW5zdGFsbCB0aGUgbW9kdWxlcyBpbiByZXF1aXJlbWVudHMudHh0IikNCiAgICBleGl0KCkNCiAgICANCmNsYXNzIHNwb3RpZnk6DQoNCiAgICBkZWYgX19pbml0X18oc2VsZiwgcHJvZmlsZSwgcHJveHkgPSBOb25lKToNCiAgICAgICAgc2VsZi5zZXNzaW9uID0gcmVxdWVzdHMuU2Vzc2lvbigpDQogICAgICAgIHNlbGYucHJvZmlsZSA9IHByb2ZpbGUNCiAgICAgICAgc2VsZi5wcm94eSA9IHByb3h5DQogICAgDQogICAgZGVmIHJlZ2lzdGVyX2FjY291bnQoc2VsZik6DQogICAgICAgIGhlYWRlcnMgPSB7DQogICAgICAgICAgICAiQWNjZXB0IjogIiovKiIsDQogICAgICAgICAgICAiUWV6eSI6ICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvODcuMC40MjgwLjE0MSBTYWZhcmkvNTM3LjM2IiwNCiAgICAgICAgICAgICJDb250ZW50LVR5cGUiOiAiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiwNCiAgICAgICAgICAgICJSZWZlcmVyIjogImh0dHBzOi8vd3d3LnNwb3RpZnkuY29tLyINCiAgICAgICAgfQ0KICAgICAgICBlbWFpbCA9ICgiIikuam9pbihyYW5kb20uY2hvaWNlcyhzdHJpbmcuYXNjaWlfbGV0dGVycyArIHN0cmluZy5kaWdpdHMsIGsgPSA4KSkgKyAiQG91dGxvb2suY28uaWQiDQogICAgICAgIHBhc3N3b3JkID0gKCIiKS5qb2luKHJhbmRvbS5jaG9pY2VzKHN0cmluZy5hc2NpaV9sZXR0ZXJzICsgc3RyaW5nLmRpZ2l0cywgayA9IDgpKQ0KICAgICAgICBwcm94aWVzID0gTm9uZQ0KICAgICAgICBpZiBzZWxmLnByb3h5ICE9IE5vbmU6DQogICAgICAgICAgICBwcm94aWVzID0geyJodHRwcyI6IGYiaHR0cDovL3tzZWxmLnByb3h5fSJ9DQogICAgICAgIGRhdGEgPSBmImJpcnRoX2RheT0xJmJpcnRoX21vbnRoPTAxJmJpcnRoX3llYXI9MTk3MCZjb2xsZWN0X3BlcnNvbmFsX2luZm89dW5kZWZpbmVkJmNyZWF0aW9uX2Zsb3c9JmNyZWF0aW9uX3BvaW50PWh0dHBzOi8vd3d3LnNwb3RpZnkuY29tL3VrLyZkaXNwbGF5bmFtZT1kZW9mZnVzY2F0ZWQmZW1haWw9e2VtYWlsfSZnZW5kZXI9bmV1dHJhbCZpYWdyZ'
love = 'JH9ZFMeMKx9LGSyAQt2MGV3ZwyzAQMxAzWvZmL4MQMvZzWwMTRmZwLzpTSmp3qipzD9r3Oup3A3o3WxsFMjLKAmq29lMS9lMKOyLKD9r3Oup3A3o3WxsFMjoTS0Mz9loG13q3pzpzIzMKWlMKV9WaAyozDgMJ1unJj9ZFM0nTylMUOupaE5MJ1unJj9ZPMzLw0jVt0XVPNtVPNtVPO0pax6QDbtVPNtVPNtVPNtVPOwpzIuqTHtCFOmMJkzYaAyp3Aco24hpT9mqPtvnUE0pUZ6Yl9mpTAfnJIhqP53Ml5mpT90nJM5YzAioF9mnJqhqKNipUIvoTywY3LkY2SwL291oaDvYPObMJSxMKWmVQ0tnTIuMTIlpljtMTS0LFN9VTEuqTRfVUOlo3ucMKZtCFOjpz94nJImXD0XVPNtVPNtVPNtVPNtnJLtVzkiM2yhK3Ein2IhVvOcovOwpzIuqTHhqTI4qQbAPvNtVPNtVPNtVPNtVPNtVPOfo2qcoy90o2gyovN9VTAlMJS0MF5dp29hXPyoW2kiM2yhK3Ein2IhW10APvNtVPNtVPNtVPNtVPNtVPO3nKEbVT9jMJ4bVxAlMJS0MJDhqUu0VvjtVzRvXFOuplOzBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPOzYaqlnKEyXTLar2IgLJyfsGc7pTSmp3qipzE9Bagfo2qcoy90o2gyoa1povpcQDbtVPNtVPNtVPNtVPNtVPNtpzI0qKWhVTkiM2yhK3Ein2IhQDbtVPNtVPNtVPNtVPOyoUAyBt0XVPNtVPNtVPNtVPNtVPNtVUWyqUIlovOBo25yQDbtVPNtVPNtVTI4L2IjqQbAPvNtVPNtVPNtVPNtVUWyqUIlovOTLJkmMD0XQDbtVPNtMTIzVTqyqS9wp3WzK3Ein2IhXUAyoTLcBt0XVPNtVPNtVPO0pax6QDbtVPNtVPNtVPNtVPOlVQ0tp2IfMv5mMKAmnJ9hYzqyqPtvnUE0pUZ6Yl93q3php3OiqTyzrF5wo20iqJfip2yaoaIjYm9zo3W3LKWxK3IloQ1bqUEjpmbiY2SwL291oaEmYaAjo3EcMaxhL29gY2IhY3A0LKE1plMmpS90K2AiqJ50MKV9ZFVcQDbtVPNtVPNtVPNtVPOlMKE1pz4tpv50MKu0YaAjoTy0XPqwp3WzIT9eMJ4vBvVaXIfkKF5mpTkcqPtaVvpcJmOqQDbtVPNtVPNtVTI4L2IjqQbAPvNtVPNtVPNtVPNtVUWyqUIlovOBo25yQDbtVPNtVPNtVN0XVPNtVTEyMvOaMKEsqT9eMJ4bp2IfMvjtoT9anJ5sqT9eMJ4cBt0XVPNtVPNtVPObMJSxMKWmVQ0trj0XVPNtVPNtVPNtVPNtVxSwL2IjqPV6VPVdYlbvYN0XVPNtVPNtVPNtVPNtVySyraxvBvNvGJ96nJkfLF81YwNtXSqcozEiq3ZtGyDtZGNhZQftI2yhAwD7VUt2APxtDKOjoTIKMJWYnKDiAGZ3YwZ2VPuYFSEAGPjtoTyeMFOUMJAeolxtD2ulo21yYmt3YwNhAQV4ZP4kAQRtH2SzLKWcYmHmAl4mAvVfQDbtVPNtVPNtVPNtVPNvD29hqTIhqP1HrK'
god = 'BlIjogImFwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZCIsDQogICAgICAgICAgICAiWC1DU1JGLVRva2VuIjogc2VsZi5nZXRfY3NyZl90b2tlbigpLA0KICAgICAgICAgICAgIkhvc3QiOiAid3d3LnNwb3RpZnkuY29tIg0KICAgICAgICB9DQogICAgICAgIHNlbGYuc2Vzc2lvbi5wb3N0KCJodHRwczovL3d3dy5zcG90aWZ5LmNvbS9hcGkvc2lnbnVwL2F1dGhlbnRpY2F0ZSIsIGhlYWRlcnMgPSBoZWFkZXJzLCBkYXRhID0gInNwbG90PSIgKyBsb2dpbl90b2tlbikNCiAgICAgICAgaGVhZGVycyA9IHsNCiAgICAgICAgICAgICJhY2NlcHQiOiAiYXBwbGljYXRpb24vanNvbiIsDQogICAgICAgICAgICAiQWNjZXB0LUVuY29kaW5nIjogImd6aXAsIGRlZmxhdGUsIGJyIiwNCiAgICAgICAgICAgICJhY2NlcHQtbGFuZ3VhZ2UiOiAiZW4iLA0KICAgICAgICAgICAgIlFlenkiOiAiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg3LjAuNDI4MC4xNDEgU2FmYXJpLzUzNy4zNiIsDQogICAgICAgICAgICAic3BvdGlmeS1hcHAtdmVyc2lvbiI6ICIxLjEuNTIuMjA0LmdlNDNiYzQwNSIsDQogICAgICAgICAgICAiYXBwLXBsYXRmb3JtIjogIldlYlBsYXllciIsDQogICAgICAgICAgICAiSG9zdCI6ICJvcGVuLnNwb3RpZnkuY29tIiwNCiAgICAgICAgICAgICJSZWZlcmVyIjogImh0dHBzOi8vb3Blbi5zcG90aWZ5LmNvbS8iDQogICAgICAgIH0NCiAgICAgICAgdHJ5Og0KICAgICAgICAgICAgciA9IHNlbGYuc2Vzc2lvbi5nZXQoDQogICAgICAgICAgICAgICAgImh0dHBzOi8vb3Blbi5zcG90aWZ5LmNvbS9nZXRfYWNjZXNzX3Rva2VuP3JlYXNvbj10cmFuc3BvcnQmcHJvZHVjdFR5cGU9d2ViX3BsYXllciIsDQogICAgICAgICAgICAgICAgaGVhZGVycyA9IGhlYWRlcnMNCiAgICAgICAgICAgICkNCiAgICAgICAgICAgIHJldHVybiByLmpzb24oKVsiYWNjZXNzVG9rZW4iXQ0KICAgICAgICBleGNlcHQ6DQogICAgICAgICAgICByZXR1cm4gTm9uZQ0KDQogICAgZGVmIGZvbGxvdyhzZWxmKToNCiAgICAgICAgaWYgIi91c2VyLyIgaW4gc2VsZi5wcm9maWxlOg0KICAgICAgICAgICAgc2VsZi5wcm9maWxlID0gc2VsZi5wcm9maWxlLnNwbGl0KCIvdXNlci8iKVsxXQ0KICAgICAgICBpZiAiPyIgaW4gc2VsZi5wcm9maWxlOg0KICAgICAgICA'
destiny = 'tVPNtp2IfMv5jpz9znJkyVQ0tp2IfMv5jpz9znJkyYaAjoTy0XPV/VvyoZS0APvNtVPNtVPNtoT9anJ5sqT9eMJ4tCFOmMJkzYaWyM2ymqTIlK2SwL291oaDbXD0XVPNtVPNtVPOcMvOfo2qcoy90o2gyovN9CFOBo25yBt0XVPNtVPNtVPNtVPNtpzI0qKWhVR5iozHfVPWoHxSHEHkWGHyHKFO3nTyfMFOlMJqcp3EypzyhMlVAPvNtVPNtVPNtMJkcMvOfo2qcoy90o2gyovN9CFOTLJkmMGbAPvNtVPNtVPNtVPNtVUWyqUIlovOBo25yYPOzVzWuMPOjpz94rFOiovOlMJqcp3EypvO7p2IfMv5jpz94rK0vQDbtVPNtVPNtVTS1qTusqT9eMJ4tCFOmMJkzYzqyqS90o2gyovufo2qcoy90o2gyovxAPvNtVPNtVPNtnJLtLKI0nS90o2gyovN9CFOBo25yBt0XVPNtVPNtVPNtVPNtpzI0qKWhVR5iozHfVPW3nTyfMFOaMKE0nJ5aVTS1qTttqT9eMJ4vQDbtVPNtVPNtVTuyLJEypaZtCFO7QDbtVPNtVPNtVPNtVPNvLJAwMKO0VwbtVzSjpTkcL2S0nJ9hY2cmo24vYN0XVPNtVPNtVPNtVPNtVxSwL2IjqP1SozAiMTyhMlV6VPWarzyjYPOxMJMfLKEyYPOvpvVfQDbtVPNtVPNtVPNtVPNvLJAwMKO0YJkuozq1LJqyVwbtVzIhVvjAPvNtVPNtVPNtVPNtVPWEMKc5VwbtVx1irzyfoTRiAF4jVPuKnJ5xo3qmVR5HVQRjYwN7VSqcowL0BlO4AwDcVRSjpTkyI2IvF2y0YmHmAl4mAvNbF0uHGHjfVTkcn2HtE2Iwn28cVRAbpz9gMF84Al4jYwDlBQNhZGDkVSAuMzSlnF81ZmphZmLvYN0XVPNtVPNtVPNtVPNtVzSjpP1joTS0Mz9loFV6VPWKMJWDoTS5MKVvYN0XVPNtVPNtVPNtVPNtVyWyMzIlMKVvBvNvnUE0pUZ6Yl9ipTIhYaAjo3EcMaxhL29gYlVfQDbtVPNtVPNtVPNtVPNvp3OiqTyzrF1upUNgqzIlp2yiovV6VPVkYwRhAGVhZwN0YzqyAQAvLmDjAFVfQDbtVPNtVPNtVPNtVPNvLKI0nT9lnKcuqTyiovV6VPWPMJSlMKVtr30vYzMipz1uqPuuqKEbK3Ein2IhXFjAPvNtVPNtVPNtsD0XVPNtVPNtVPO0pax6QDbtVPNtVPNtVPNtVPOmMJkzYaAyp3Aco24hpUI0XN0XVPNtVPNtVPNtVPNtVPNtVPWbqUEjpmbiY2SjnF5mpT90nJM5YzAioF92ZF9gMF9zo2kfo3qcozp/qUyjMG11p2IlWzyxpm0vVPftp2IfMv5jpz9znJkyYN0XVPNtVPNtVPNtVPNtVPNtVTuyLJEypaZtCFObMJSxMKWmQDbtVPNtVPNtVPNtVPNcQDbtVPNtVPNtVPNtVPOlMKE1pz4tIUW1MFjtGz9hMD0XVPNtVPNtVPOyrTAypUD6QDbtVPNtVPNtVPNtVPOlMKE1pz4tEzSfp2HfVPW3nTyfMFOzo2kfo3qcozpvQDbAPt0X'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

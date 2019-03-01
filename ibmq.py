from IBMQuantumExperience import IBMQuantumExperience
api_key = "d4e0b2c7a9152ebb69d8af1c05b8d4e2a31321e555cb70e085dff4408af2f797bf55125919276ba5296daf31d3a7db517830424ab583f7c2c34f0a72138dc58d"
config = {
   "url": 'https://quantumexperience.ng.bluemix.net/api'
}

# If verify is set to False, ignore SSL certificate errors:
api = IBMQuantumExperience(api_key,config,verify=True)

# print available backends
# print(api.available_backends())

backend = "ibmqx4"

# get backend_parameters
# print(api.backend_parameters(backend))

# running parameters
qasms=[
#    { 'qasm': 'OPENQASM 2.0;\n\ninclude "qelib1.inc";\nqreg q[5];\ncreg c[5];\nh q[0];\ncx q[0],q[2];\nmeasure q[0] -> c[0];\nmeasure q[2] -> c[1];\n'},
   { 'qasm': 'OPENQASM 2.0;\n\ninclude "qelib1.inc";\nqreg q[5];\ncreg c[5];\nx q[0];\nmeasure q[0] -> c[0];\n'}
]

max_credits = 3

shots=1024

# notice! we can't run job over the Unit
# print(api.run_job(qasms, backend, shots, max_credits))

# get job information
job_id = '5c79328444a7180054744fcd'
print(api.get_job(job_id))


# jpb limit
# limit=5
# print(api.get_jobs(limit))







# qasm = 'OPENQASM 2.0;\n\ninclude "qelib1.inc";\nqreg q[5];\ncreg c[5];\nh q[0];\ncx q[0],q[2];\nmeasure q[0] -> c[0];\nmeasure q[2] -> c[1];\n'
# device = 'ibmqx4'
# shots=1024
# name="test190301"
# timeout=60

# api.run_experiment(qasm, device, shots, name, timeout)



# print(my_credit)
# print(my_code)

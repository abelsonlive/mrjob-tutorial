from word_counts import MRWordCounter
args = [
    "-r", "local", 
    "s3://abelson-emr/sample_data/", 
    "-c", "../mrjob.yml"]
job = MRWordCounter(args=args)
job.run_job()

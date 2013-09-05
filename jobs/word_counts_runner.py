from word_counts import MRIndexScraper
args = [
    "-r", "local", "data/" 
    # "s3://abelson-emr/sample_data/", 
    # "-c", "../mrjob.yml",
    # "--no-output", "output-dir=s3://abelson-emr/output_data/"
]
job = MRWordCounter(args=args)
job.run_job()

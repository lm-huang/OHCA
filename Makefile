.PHONY: clean

preprocess.db:
	mkdir -p data
	python -B src/preprocess_data.py


imputation: data/nemsis.db
	python -B src/imputation.py

response-time: data/nemsis.db
	python -B src/response_time_diff.py
	python -B src/scale_diff.py

AEDCPR: data/nemsis.db
	python -B src/AED_CPR.py

xgb: data/nemsis.db
	python -B src/xgb.py

clean:
	rm data/nemsis.db
	rm data/imputed-features.csv
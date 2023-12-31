
import recorder
import generator

def main():
	# run the recorder
	map_file = "Lidar-Slam-Simulation-master\map2.png";
	recorder.record(map_file);

	# run the generator
	laser_range = 1000; # in pixels
	num_lasers = 360;
	generator.generate(laser_range, num_lasers);

if __name__ == "__main__":
	main();
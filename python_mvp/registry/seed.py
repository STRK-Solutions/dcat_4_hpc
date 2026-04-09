from __future__ import annotations

from .services import Registry


def seed_mock_data(registry: Registry) -> None:
	"""Populate the registry with Agriculture Canada–style example data products."""

	# Teams (display names)
	climate_team = registry.create_team("Climate & Environment")
	crops_team = registry.create_team("Crop Analytics")

	# Data products
	climate_obs_dp = registry.create_data_product(
		name="canada_climate_observations_daily",
		description="Daily climate observations aggregated from Environment Canada weather stations.",
		owner_team_id=climate_team.teams_id,
		data_format="parquet",
		access_uri="/publish/climate_environment/canada_climate_observations_daily",
		status="active",
		classification="public",
	)

	crop_yield_dp = registry.create_data_product(
		name="crop_yield_forecast_grid",
		description="Grid-level crop yield forecasts derived from historical yield data and climate indicators.",
		owner_team_id=crops_team.teams_id,
		data_format="geoparquet",
		access_uri="/publish/crop_analytics/crop_yield_forecast_grid",
		status="active",
		classification="internal",
	)

	# Metadata for climate observations
	registry.add_metadata(
		data_product_id=climate_obs_dp.product_id,
		namespace="business",
		meta_key="domain",
		meta_value="climate",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=climate_obs_dp.product_id,
		namespace="technical",
		meta_key="spatial_resolution",
		meta_value="station-level",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=climate_obs_dp.product_id,
		namespace="technical",
		meta_key="refresh_schedule",
		meta_value="0 6 * * *",
		value_type="cron",
	)
	registry.add_metadata(
		data_product_id=climate_obs_dp.product_id,
		namespace="governance",
		meta_key="source",
		meta_value="Environment and Climate Change Canada",
		value_type="string",
	)

	# Metadata for crop yield forecast
	registry.add_metadata(
		data_product_id=crop_yield_dp.product_id,
		namespace="business",
		meta_key="domain",
		meta_value="agriculture",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=crop_yield_dp.product_id,
		namespace="technical",
		meta_key="grid_system",
		meta_value="10km x 10km national grid",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=crop_yield_dp.product_id,
		namespace="technical",
		meta_key="model_type",
		meta_value="regression + climate indicators",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=crop_yield_dp.product_id,
		namespace="governance",
		meta_key="intended_use",
		meta_value="research and policy analysis",
		value_type="string",
	)


	# ---------------------------------------------------------------------
	# Additional Data Products
	# ---------------------------------------------------------------------

	# Soil moisture index
	soil_moisture_dp = registry.create_data_product(
		name="soil_moisture_index_weekly",
		description="Weekly soil moisture index derived from satellite and in-situ sensor data.",
		owner_team_id=climate_team.teams_id,
		data_format="parquet",
		access_uri="/publish/climate_environment/soil_moisture_index_weekly",
		status="active",
		classification="internal",
	)

	registry.add_metadata(
		data_product_id=soil_moisture_dp.product_id,
		namespace="business",
		meta_key="domain",
		meta_value="climate",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=soil_moisture_dp.product_id,
		namespace="technical",
		meta_key="spatial_resolution",
		meta_value="5km grid",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=soil_moisture_dp.product_id,
		namespace="technical",
		meta_key="refresh_schedule",
		meta_value="0 3 * * 1",
		value_type="cron",
	)
	registry.add_metadata(
		data_product_id=soil_moisture_dp.product_id,
		namespace="governance",
		meta_key="source",
		meta_value="Canadian Soil Monitoring Network",
		value_type="string",
	)

	# Livestock population statistics
	livestock_dp = registry.create_data_product(
		name="livestock_population_statistics",
		description="Quarterly livestock population counts across Canadian provinces.",
		owner_team_id=crops_team.teams_id,
		data_format="delta",
		access_uri="/publish/crop_analytics/livestock_population_statistics",
		status="active",
		classification="restricted",
	)

	registry.add_metadata(
		data_product_id=livestock_dp.product_id,
		namespace="business",
		meta_key="domain",
		meta_value="agriculture",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=livestock_dp.product_id,
		namespace="technical",
		meta_key="spatial_resolution",
		meta_value="province-level",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=livestock_dp.product_id,
		namespace="technical",
		meta_key="refresh_schedule",
		meta_value="0 2 1 */3 *",
		value_type="cron",
	)
	registry.add_metadata(
		data_product_id=livestock_dp.product_id,
		namespace="governance",
		meta_key="intended_use",
		meta_value="policy development and economic forecasting",
		value_type="string",
	)

	# Satellite NDVI timeseries
	ndvi_dp = registry.create_data_product(
		name="satellite_ndvi_timeseries",
		description="Normalized Difference Vegetation Index (NDVI) timeseries derived from satellite imagery.",
		owner_team_id=climate_team.teams_id,
		data_format="geoparquet",
		access_uri="/publish/climate_environment/satellite_ndvi_timeseries",
		status="active",
		classification="public",
	)

	registry.add_metadata(
		data_product_id=ndvi_dp.product_id,
		namespace="business",
		meta_key="domain",
		meta_value="agriculture",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=ndvi_dp.product_id,
		namespace="technical",
		meta_key="spatial_resolution",
		meta_value="250m raster",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=ndvi_dp.product_id,
		namespace="technical",
		meta_key="refresh_schedule",
		meta_value="0 4 * * 0",
		value_type="cron",
	)
	registry.add_metadata(
		data_product_id=ndvi_dp.product_id,
		namespace="governance",
		meta_key="source",
		meta_value="Sentinel-2 Satellite Imagery",
		value_type="string",
	)

	# Irrigation water usage
	irrigation_dp = registry.create_data_product(
		name="irrigation_water_usage_monthly",
		description="Monthly irrigation water usage aggregated by agricultural region.",
		owner_team_id=crops_team.teams_id,
		data_format="parquet",
		access_uri="/publish/crop_analytics/irrigation_water_usage_monthly",
		status="draft",
		classification="internal",
	)

	registry.add_metadata(
		data_product_id=irrigation_dp.product_id,
		namespace="business",
		meta_key="domain",
		meta_value="water_management",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=irrigation_dp.product_id,
		namespace="technical",
		meta_key="spatial_resolution",
		meta_value="regional-level",
		value_type="string",
	)
	registry.add_metadata(
		data_product_id=irrigation_dp.product_id,
		namespace="technical",
		meta_key="refresh_schedule",
		meta_value="0 1 1 * *",
		value_type="cron",
	)
	registry.add_metadata(
		data_product_id=irrigation_dp.product_id,
		namespace="governance",
		meta_key="intended_use",
		meta_value="water resource planning",
		value_type="string",
	)

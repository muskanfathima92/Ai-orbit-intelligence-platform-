\# AI Orbit Intelligence Platform



\## Overview



AI Orbit Intelligence Platform is a multi-source AI ecosystem discovery and intelligence system.



The platform collects information from multiple AI-related sources, processes and cleans the data, removes duplicates, resolves entities, validates the resulting records, maps evidence-backed relationships, and presents the final dataset through an interactive Streamlit dashboard.



\## Key Features



\- Multi-source AI data discovery

\- GitHub repository discovery

\- Hugging Face model discovery

\- AI news discovery

\- MCP server and AI tool data processing

\- Entity normalization

\- Data cleaning

\- Deduplication

\- Entity classification

\- Entity resolution

\- Data validation

\- Evidence-backed relationship mapping

\- Interactive Streamlit dashboard

\- Search and filtering

\- JSON and CSV export

\- Automated test suite



\## Entity Types



The platform currently handles six major entity types:



1\. Company

2\. AI Model

3\. Repository

4\. News

5\. MCP Server

6\. AI Tool



\## Pipeline Architecture



```text

&#x20;               DATA SOURCES

&#x20;                    |

&#x20;       +------------+------------+

&#x20;       |            |            |

&#x20;     GitHub    Hugging Face    News

&#x20;       |            |            |

&#x20;       +------------+------------+

&#x20;                    |

&#x20;             Raw Data Storage

&#x20;                    |

&#x20;                    v

&#x20;             Data Processing

&#x20;                    |

&#x20;       +------------+------------+

&#x20;       |            |            |

&#x20;     Cleaning   Deduplication  Classification

&#x20;       |            |            |

&#x20;       +------------+------------+

&#x20;                    |

&#x20;             Entity Resolution

&#x20;                    |

&#x20;                Validation

&#x20;                    |

&#x20;             Unified Entities

&#x20;                    |

&#x20;           Relationship Mapping

&#x20;                    |

&#x20;             Final Dataset

&#x20;                    |

&#x20;            Streamlit Dashboard

